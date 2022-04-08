# Generated by Django 3.2.9 on 2022-04-07 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powers', '0061_auto_20220407_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawback',
            name='category',
            field=models.CharField(choices=[('MOD_GIFT', 'Gift Type'), ('MOD_ACTIVATION', 'Activation / Targeting'), ('MOD_EFFECT', 'Effect')], default='MOD_EFFECT', help_text='For filtering on create gift page', max_length=30),
        ),
        migrations.AlterField(
            model_name='enhancement',
            name='category',
            field=models.CharField(choices=[('MOD_GIFT', 'Gift Type'), ('MOD_ACTIVATION', 'Activation / Targeting'), ('MOD_EFFECT', 'Effect')], default='MOD_EFFECT', help_text='For filtering on create gift page', max_length=30),
        ),
    ]
