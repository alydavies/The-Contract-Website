# Generated by Django 3.2.15 on 2022-12-10 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0091_auto_20221206_1422'),
        ('games', '0052_auto_20221206_1457'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='scenarioelement',
            unique_together={('relevant_element', 'relevant_scenario')},
        ),
    ]
