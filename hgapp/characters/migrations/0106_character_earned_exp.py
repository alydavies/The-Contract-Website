# Generated by Django 3.2.20 on 2024-02-02 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0105_auto_20231204_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='earned_exp',
            field=models.IntegerField(default=0),
        ),
    ]