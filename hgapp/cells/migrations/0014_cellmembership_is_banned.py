# Generated by Django 3.2.9 on 2022-05-14 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cells', '0013_alter_cell_use_golden_ratio'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellmembership',
            name='is_banned',
            field=models.BooleanField(default=False),
        ),
    ]
