# Generated by Django 3.2.15 on 2022-09-24 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0083_auto_20220924_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='charactertutorial',
            name='ambitions',
            field=models.JSONField(default=list),
        ),
    ]
