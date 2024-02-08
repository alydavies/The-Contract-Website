# Generated by Django 3.2.20 on 2024-02-07 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0002_auto_20240206_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='moderation_reason',
            field=models.CharField(blank=True, choices=[('OBSCENE', 'Obscene or explicit content'), ('DOX', 'Sharing personal information'), ('HARASSMENT', 'Abuse or harassment'), ('ADVERTISING', 'Unsolicited advertising or sales'), ('SPAM', 'Spam'), ('OTHER', 'Other (specify below)')], max_length=50, null=True),
        ),
    ]