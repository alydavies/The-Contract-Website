# Generated by Django 3.2.9 on 2022-07-23 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0074_auto_20220723_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='charactertutorial',
            name='loose_ends',
            field=models.TextField(default='placeholder', max_length=3000),
        ),
        migrations.AddField(
            model_name='charactertutorial',
            name='moves',
            field=models.TextField(default='placeholder', max_length=3000),
        ),
    ]
