# Generated by Django 3.2.15 on 2022-11-26 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0049_manual_primary_writeup'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='objective',
            field=models.TextField(blank=True, max_length=5000),
        ),
    ]
