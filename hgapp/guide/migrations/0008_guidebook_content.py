# Generated by Django 3.2.9 on 2022-06-22 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0007_guidepic'),
    ]

    operations = [
        migrations.AddField(
            model_name='guidebook',
            name='content',
            field=models.TextField(default=' ', max_length=74000),
            preserve_default=False,
        ),
    ]