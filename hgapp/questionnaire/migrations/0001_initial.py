# Generated by Django 3.2.15 on 2023-09-23 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0059_scenario_date_added_to_exchange'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('characters', '0100_alter_experiencereward_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('written_contract_number', models.IntegerField(default=0)),
                ('content', models.TextField(blank=True, max_length=100000, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('is_valid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt', models.CharField(max_length=400)),
                ('min_word_count', models.IntegerField(default=150)),
                ('is_repeatable', models.BooleanField(default=True)),
                ('contract_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddIndex(
            model_name='question',
            index=models.Index(fields=['contract_number'], name='questionnai_contrac_80b67d_idx'),
        ),
        migrations.AddField(
            model_name='answer',
            name='experience_reward',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='characters.experiencereward'),
        ),
        migrations.AddField(
            model_name='answer',
            name='game_attendance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game_attendance'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='relevant_character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.character'),
        ),
        migrations.AddField(
            model_name='answer',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='answer',
            index=models.Index(fields=['relevant_character'], name='questionnai_relevan_32019b_idx'),
        ),
    ]