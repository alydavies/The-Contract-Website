# Generated by Django 2.2.13 on 2021-09-05 18:40

from django.db import migrations, models
from django.db.models import Q, Count
from django.db import transaction
from bs4 import BeautifulSoup

GAME_STATUS = (
    # Invites go out, players may accept invites w/ characters and change whether they are coming and with which character
    # The scenario is chosen
    # GM specifies level, message, etc.
    ('SCHEDULED', 'Scheduled'),

    # The game is "activated". invites are invalidated. Players can no longer change which character is attending
    # Characters are closed for editing for the duration of the game
    # GMs have 24 hours from this point to declare the game finished, or individual players may void their attendance.
    ('ACTIVE', 'Active'),

    # Game is finished, GM declares all outcomes, characters are unlocked or declared dead. Game is officially over
    # Void proceedings may occur. Players may open game for void vote.
    # Characters are locked while a void vote is in progress.
    # Void votes may only last 24 hours
    # GM may declare void.
    ('FINISHED', 'Finished'),

    # After a set time peroid, or after any character is attending another game that is in the "ACTIVE" state, the void window
    # is closed. The game transitions into "ARCHIVED."
    ('ARCHIVED', 'Archived'),

    # Any game that is scheduled, can be canceled, which is an end state. All invites are voided. Attendances are erased.
    ('CANCELED', 'Canceled'),

    # All games that reach the "Active" state can be voided through verious means. Attendance remains on record, but is void.
    ('VOID', 'Void'),

    # Finalized games that were entered after-the-fact.
    ('RECORDED', 'Archived'),
)

WIN = 'WIN'
DEATH = 'DEATH'

def reverse_migrate_update_stats(apps, schema_editor):
    pass

def get_completed_game_excludes_query():
    return Q(status=GAME_STATUS[0][0]) \
           | Q(status=GAME_STATUS[1][0]) \
           | Q(status=GAME_STATUS[4][0])

def migrate_update_stats(apps, schema_editor):
    Scenario = apps.get_model('games', 'Scenario')
    Game = apps.get_model('games', 'Game')
    Game_Attendance = apps.get_model('games', 'Game_attendance')
    for scenario in Scenario.objects.all():
        with transaction.atomic():
            scenario.times_run = scenario.game_set.exclude(get_completed_game_excludes_query()).count()
            scenario.num_gms_run = Game.objects \
                .filter(scenario=scenario) \
                .exclude(get_completed_game_excludes_query()) \
                .aggregate(Count('gm_id', distinct=True))['gm_id__count']
            scenario.num_victories = Game_Attendance.objects.filter(relevant_game__scenario=scenario, outcome=WIN, is_confirmed=True).count()
            scenario.num_deaths = Game_Attendance.objects.filter(relevant_game__scenario=scenario, outcome=DEATH, is_confirmed=True).count()
            scenario.deadliness_ratio = scenario.num_deaths / max(scenario.num_victories, 1)
            soup = BeautifulSoup(scenario.description, features="html5lib")
            scenario.num_words = len(soup.text.split())
            scenario.save()

class Migration(migrations.Migration):

    dependencies = [
        ('games', '0038_auto_20211024_1846'),
    ]

    operations = [
        migrations.RunPython(migrate_update_stats, reverse_migrate_update_stats),
    ]