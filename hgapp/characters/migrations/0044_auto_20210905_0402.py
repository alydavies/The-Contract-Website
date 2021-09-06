# Generated by Django 2.2.13 on 2021-09-05 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0043_contract_game_stats'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='character',
            index=models.Index(fields=['num_victories', 'private'], name='characters__num_vic_d10baf_idx'),
        ),
        migrations.AddIndex(
            model_name='character',
            index=models.Index(fields=['num_losses', 'private'], name='characters__num_los_c7b3bf_idx'),
        ),
        migrations.AddIndex(
            model_name='character',
            index=models.Index(fields=['num_games', 'private'], name='characters__num_gam_5ef174_idx'),
        ),
        migrations.AddIndex(
            model_name='character',
            index=models.Index(fields=['player'], name='characters__player__8f5c3c_idx'),
        ),
    ]