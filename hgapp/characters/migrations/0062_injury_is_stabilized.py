# Generated by Django 3.2.9 on 2022-02-09 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0061_alter_weapon_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='injury',
            name='is_stabilized',
            field=models.BooleanField(default=False),
        ),
    ]
