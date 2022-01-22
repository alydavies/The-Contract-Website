# Generated by Django 3.2.9 on 2021-12-30 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('powers', '0029_systemfieldroll_caster_rolls'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasePowerFieldSubstitution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replacement', models.CharField(blank=True, help_text="A '$' in this string will be replaced with user input", max_length=350)),
                ('mode', models.CharField(choices=[('EPHEMERAL', 'Ephemeral'), ('UNIQUE', 'Unique'), ('ADDITIVE', 'Additive')], default='ADDITIVE', max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DrawbackFieldSubstitution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replacement', models.CharField(blank=True, help_text="A '$' in this string will be replaced with user input", max_length=350)),
                ('mode', models.CharField(choices=[('EPHEMERAL', 'Ephemeral'), ('UNIQUE', 'Unique'), ('ADDITIVE', 'Additive')], default='ADDITIVE', max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EnhancementFieldSubstitution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replacement', models.CharField(blank=True, help_text="A '$' in this string will be replaced with user input", max_length=350)),
                ('mode', models.CharField(choices=[('EPHEMERAL', 'Ephemeral'), ('UNIQUE', 'Unique'), ('ADDITIVE', 'Additive')], default='ADDITIVE', max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FieldSubstitutionMarker',
            fields=[
                ('marker', models.SlugField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ParameterFieldSubstitution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replacement', models.CharField(blank=True, help_text="A '$' in this string will be replaced with user input", max_length=350)),
                ('mode', models.CharField(choices=[('EPHEMERAL', 'Ephemeral'), ('UNIQUE', 'Unique'), ('ADDITIVE', 'Additive')], default='ADDITIVE', max_length=25)),
                ('relevant_marker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='powers.fieldsubstitutionmarker')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PowerHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='base_power',
            options={'verbose_name': 'Gift Component'},
        ),
        migrations.AlterModelOptions(
            name='power_full',
            options={'permissions': (('view_private_power_full', 'View private power full'), ('edit_power_full', 'Edit power full')), 'verbose_name': 'Gift'},
        ),
        migrations.RemoveField(
            model_name='base_power',
            name='default_activation_style',
        ),
        migrations.RemoveField(
            model_name='power',
            name='linked_powers',
        ),
        migrations.RemoveField(
            model_name='power_full',
            name='linked_powers',
        ),
        migrations.AddField(
            model_name='base_power',
            name='allowed_modalities',
            field=models.ManyToManyField(blank=True, help_text='Set on Effects only. No effect on Vectors or Modalities.', related_name='vector_modalities', to='powers.Base_Power'),
        ),
        migrations.AddField(
            model_name='base_power',
            name='allowed_vectors',
            field=models.ManyToManyField(blank=True, help_text='Set on Effects and Modalities only. No effect on Vectors.', related_name='vector_effects', to='powers.Base_Power'),
        ),
        migrations.AddField(
            model_name='base_power',
            name='avail_drawbacks',
            field=models.ManyToManyField(blank=True, related_name='avail_drawbacks', to='powers.Drawback', verbose_name='drawbacks'),
        ),
        migrations.AddField(
            model_name='base_power',
            name='avail_enhancements',
            field=models.ManyToManyField(blank=True, related_name='avail_enhancements', to='powers.Enhancement', verbose_name='enhancements'),
        ),
        migrations.AddField(
            model_name='base_power',
            name='base_type',
            field=models.CharField(choices=[('EFFECT', 'Effect'), ('VECTOR', 'Vector'), ('MODALITY', 'Modality')], default='EFFECT', help_text='DO NOT CHANGE THIS AFTER INITIAL CREATION', max_length=25, verbose_name='component type'),
        ),
        migrations.AddField(
            model_name='base_power',
            name='blacklist_drawbacks',
            field=models.ManyToManyField(blank=True, related_name='blacklist_drawbacks', to='powers.Drawback'),
        ),
        migrations.AddField(
            model_name='base_power',
            name='blacklist_enhancements',
            field=models.ManyToManyField(blank=True, related_name='blacklist_enhancements', to='powers.Enhancement'),
        ),
        migrations.AddField(
            model_name='base_power',
            name='blacklist_parameters',
            field=models.ManyToManyField(blank=True, related_name='blacklist_params', to='powers.Parameter'),
        ),
        migrations.AddField(
            model_name='power',
            name='modality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='power_modality', to='powers.base_power'),
        ),
        migrations.AddField(
            model_name='power',
            name='vector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='power_vector', to='powers.base_power'),
        ),
        migrations.AddField(
            model_name='power_param',
            name='dice_system',
            field=models.CharField(choices=[('ALL', 'All'), ('HOUSEGAMES15', 'House Games 1.5'), ('PS2', 'New Powers System')], default='HOUSEGAMES15', max_length=55),
        ),
        migrations.AddField(
            model_name='power_param',
            name='eratta',
            field=models.TextField(blank=True, help_text='Only used by new Powers system. Ignored in old system.', null=True),
        ),
        migrations.AddField(
            model_name='power_param',
            name='level_five',
            field=models.CharField(blank=True, help_text='Only used by new Powers system. Ignored in old system.', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='power_param',
            name='level_four',
            field=models.CharField(blank=True, help_text='Only used by new Powers system. Ignored in old system.', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='power_param',
            name='level_one',
            field=models.CharField(blank=True, help_text='Only used by new Powers system. Ignored in old system.', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='power_param',
            name='level_six',
            field=models.CharField(blank=True, help_text='Only used by new Powers system. Ignored in old system.', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='power_param',
            name='level_three',
            field=models.CharField(blank=True, help_text='Only used by new Powers system. Ignored in old system.', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='power_param',
            name='level_two',
            field=models.CharField(blank=True, help_text='Only used by new Powers system. Ignored in old system.', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='power_param',
            name='level_zero',
            field=models.CharField(blank=True, help_text='Only used by new Powers system. Ignored in old system.', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='base_power',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='powers.base_power_category'),
        ),
        migrations.AlterField(
            model_name='base_power',
            name='drawbacks',
            field=models.ManyToManyField(blank=True, to='powers.Drawback', verbose_name='legacy drawbacks'),
        ),
        migrations.AlterField(
            model_name='base_power',
            name='enhancements',
            field=models.ManyToManyField(blank=True, to='powers.Enhancement', verbose_name='legacy enhancements'),
        ),
        migrations.AlterField(
            model_name='base_power',
            name='num_free_enhancements',
            field=models.IntegerField(default=0, verbose_name='gift point credit'),
        ),
        migrations.AlterField(
            model_name='base_power',
            name='required_status',
            field=models.CharField(choices=[('ANY', 'Any'), ('NEWBIE', 'Newbie'), ('NOVICE', 'Novice'), ('SEASONED', 'Seasoned'), ('VETERAN', 'Veteran')], default='ANY', max_length=25),
        ),
        migrations.AlterField(
            model_name='base_power_system',
            name='dice_system',
            field=models.CharField(choices=[('ALL', 'All'), ('HOUSEGAMES15', 'House Games 1.5'), ('PS2', 'New Powers System')], default='PS2', max_length=55),
        ),
        migrations.AlterField(
            model_name='drawback',
            name='required_status',
            field=models.CharField(choices=[('ANY', 'Any'), ('NEWBIE', 'Newbie'), ('NOVICE', 'Novice'), ('SEASONED', 'Seasoned'), ('VETERAN', 'Veteran')], default='ANY', max_length=25),
        ),
        migrations.AlterField(
            model_name='drawback',
            name='system',
            field=models.CharField(choices=[('ALL', 'All'), ('HOUSEGAMES15', 'House Games 1.5'), ('PS2', 'New Powers System')], default='PS2', max_length=55),
        ),
        migrations.AlterField(
            model_name='enhancement',
            name='required_status',
            field=models.CharField(choices=[('ANY', 'Any'), ('NEWBIE', 'Newbie'), ('NOVICE', 'Novice'), ('SEASONED', 'Seasoned'), ('VETERAN', 'Veteran')], default='ANY', max_length=25),
        ),
        migrations.AlterField(
            model_name='enhancement',
            name='system',
            field=models.CharField(choices=[('ALL', 'All'), ('HOUSEGAMES15', 'House Games 1.5'), ('PS2', 'New Powers System')], default='PS2', max_length=55),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='eratta',
            field=models.TextField(blank=True, help_text='IGNORED IN NEW POWERS SYSTEM. Use field on Power_Param instead.', null=True),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='level_five',
            field=models.CharField(blank=True, help_text='IGNORED IN NEW POWERS SYSTEM. Use field on Power_Param instead.', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='level_four',
            field=models.CharField(blank=True, help_text='IGNORED IN NEW POWERS SYSTEM. Use field on Power_Param instead.', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='level_one',
            field=models.CharField(blank=True, help_text='IGNORED IN NEW POWERS SYSTEM. Use field on Power_Param instead.', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='level_six',
            field=models.CharField(blank=True, help_text='IGNORED IN NEW POWERS SYSTEM. Use field on Power_Param instead.', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='level_three',
            field=models.CharField(blank=True, help_text='IGNORED IN NEW POWERS SYSTEM. Use field on Power_Param instead.', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='level_two',
            field=models.CharField(blank=True, help_text='IGNORED IN NEW POWERS SYSTEM. Use field on Power_Param instead.', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='level_zero',
            field=models.CharField(help_text='IGNORED IN NEW POWERS SYSTEM. Use field on Power_Param instead.', max_length=60),
        ),
        migrations.AlterField(
            model_name='power',
            name='activation_style',
            field=models.CharField(choices=[('PASSIVE', 'Passive'), ('ACTIVE', 'Active')], default='PASSIVE', max_length=25),
        ),
        migrations.AlterField(
            model_name='power',
            name='base',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='power_effect', to='powers.base_power'),
        ),
        migrations.AlterField(
            model_name='power',
            name='description',
            field=models.TextField(max_length=2500),
        ),
        migrations.AlterField(
            model_name='power',
            name='dice_system',
            field=models.CharField(choices=[('ALL', 'All'), ('HOUSEGAMES15', 'House Games 1.5'), ('PS2', 'New Powers System')], max_length=55),
        ),
        migrations.AlterField(
            model_name='power',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='power',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='power',
            name='system',
            field=models.TextField(blank=True, max_length=14000, null=True),
        ),
        migrations.AlterField(
            model_name='power_full',
            name='dice_system',
            field=models.CharField(choices=[('ALL', 'All'), ('HOUSEGAMES15', 'House Games 1.5'), ('PS2', 'New Powers System')], max_length=55),
        ),
        migrations.AlterField(
            model_name='power_full',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='systemfieldroll',
            name='difficulty',
            field=models.PositiveIntegerField(blank=True, help_text='Not used in new Powers system', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='power_param',
            unique_together={('relevant_parameter', 'relevant_base_power', 'dice_system')},
        ),
        migrations.DeleteModel(
            name='Power_Link',
        ),
        migrations.AddField(
            model_name='powerhistory',
            name='latest_rev',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='powers.power'),
        ),
        migrations.AddField(
            model_name='powerhistory',
            name='parent_power',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='powers.power_full'),
        ),
        migrations.AddField(
            model_name='parameterfieldsubstitution',
            name='relevant_parameter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='powers.parameter'),
        ),
        migrations.AddField(
            model_name='enhancementfieldsubstitution',
            name='relevant_enhancement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='powers.enhancement'),
        ),
        migrations.AddField(
            model_name='enhancementfieldsubstitution',
            name='relevant_marker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='powers.fieldsubstitutionmarker'),
        ),
        migrations.AddField(
            model_name='drawbackfieldsubstitution',
            name='relevant_drawback',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='powers.drawback'),
        ),
        migrations.AddField(
            model_name='drawbackfieldsubstitution',
            name='relevant_marker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='powers.fieldsubstitutionmarker'),
        ),
        migrations.AddField(
            model_name='basepowerfieldsubstitution',
            name='relevant_base_power',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='powers.base_power'),
        ),
        migrations.AddField(
            model_name='basepowerfieldsubstitution',
            name='relevant_marker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='powers.fieldsubstitutionmarker'),
        ),
        migrations.AddField(
            model_name='base_power',
            name='substitutions',
            field=models.ManyToManyField(through='powers.BasePowerFieldSubstitution', to='powers.FieldSubstitutionMarker'),
        ),
        migrations.AddField(
            model_name='drawback',
            name='substitutions',
            field=models.ManyToManyField(through='powers.DrawbackFieldSubstitution', to='powers.FieldSubstitutionMarker'),
        ),
        migrations.AddField(
            model_name='enhancement',
            name='substitutions',
            field=models.ManyToManyField(through='powers.EnhancementFieldSubstitution', to='powers.FieldSubstitutionMarker'),
        ),
        migrations.AddField(
            model_name='parameter',
            name='substitutions',
            field=models.ManyToManyField(through='powers.ParameterFieldSubstitution', to='powers.FieldSubstitutionMarker'),
        ),
        migrations.AddField(
            model_name='power',
            name='power_history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='powers.powerhistory'),
        ),
    ]