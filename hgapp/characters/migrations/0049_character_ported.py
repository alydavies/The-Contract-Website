# Generated by Django 2.2.13 on 2021-09-25 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0048_auto_20210909_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='ported',
            field=models.CharField(choices=[('NOT_PORTED', 'Not ported'), ('SEASONED_PORTED', 'ported as Seasoned'), ('VETERAN_PORTED', 'ported as Veteran')], default='NOT_PORTED', max_length=50),
        ),
    ]