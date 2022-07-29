# Generated by Django 3.2.9 on 2022-07-25 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0076_looseend_threat_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='looseend',
            name='how_to_tie_up',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='looseend',
            name='original_cutoff',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='artifact',
            name='system',
            field=models.CharField(blank=True, help_text='Threat for Loose Ends', max_length=5000),
        ),
        migrations.AlterField(
            model_name='circumstance',
            name='system',
            field=models.CharField(blank=True, help_text='Threat for Loose Ends', max_length=5000),
        ),
        migrations.AlterField(
            model_name='condition',
            name='system',
            field=models.CharField(blank=True, help_text='Threat for Loose Ends', max_length=5000),
        ),
        migrations.AlterField(
            model_name='looseend',
            name='system',
            field=models.CharField(blank=True, help_text='Threat for Loose Ends', max_length=5000),
        ),
        migrations.AlterField(
            model_name='stockworldelement',
            name='system',
            field=models.CharField(blank=True, help_text='Threat for Loose Ends', max_length=1000),
        ),
    ]
