# Generated by Django 3.2.15 on 2022-10-15 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0044_auto_20220722_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='invite_all_members',
            field=models.BooleanField(default=False),
        ),
    ]