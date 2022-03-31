# Generated by Django 3.2.9 on 2022-03-15 01:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('powers', '0052_auto_20220314_0236'),
    ]

    operations = [
        migrations.CreateModel(
            name='PowerSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json_media', models.FileField(blank=True, upload_to='')),
                ('revision', models.UUIDField(default=uuid.uuid4)),
            ],
        ),
    ]