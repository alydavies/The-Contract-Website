# Generated by Django 2.2.13 on 2021-04-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0031_auto_20210418_2033'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='abilityvalue',
            index=models.Index(fields=['previous_revision'], name='characters__previou_5b58e3_idx'),
        ),
        migrations.AddIndex(
            model_name='attributevalue',
            index=models.Index(fields=['previous_revision'], name='characters__previou_95dcce_idx'),
        ),
    ]