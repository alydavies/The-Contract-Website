# Generated by Django 2.2.13 on 2021-09-25 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_auto_20210909_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='able_to_port',
            field=models.BooleanField(default=False),
        ),
    ]