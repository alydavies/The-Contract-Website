# Generated by Django 3.2.9 on 2022-01-17 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0055_auto_20211121_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='tagline',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
