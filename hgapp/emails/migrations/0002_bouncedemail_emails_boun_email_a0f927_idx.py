# Generated by Django 3.2.18 on 2023-10-24 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='bouncedemail',
            index=models.Index(fields=['email'], name='emails_boun_email_a0f927_idx'),
        ),
    ]