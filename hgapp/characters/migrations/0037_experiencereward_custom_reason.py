# Generated by Django 2.2.13 on 2021-07-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0036_auto_20210530_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiencereward',
            name='custom_reason',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]