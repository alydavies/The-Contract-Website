# Generated by Django 3.2.15 on 2023-08-31 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_auto_20230618_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='fakead',
            name='url',
            field=models.TextField(blank=True, max_length=20000),
        ),
    ]
