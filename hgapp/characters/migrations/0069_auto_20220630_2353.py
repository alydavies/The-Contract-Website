# Generated by Django 3.2.9 on 2022-06-30 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0068_auto_20220421_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockElementCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='artifact',
            name='deletion_reason',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='artifact',
            name='origin',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='asset',
            name='grants_scar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.stockbattlescar'),
        ),
        migrations.AddField(
            model_name='circumstance',
            name='deletion_reason',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='circumstance',
            name='origin',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='condition',
            name='deletion_reason',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='condition',
            name='origin',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='liability',
            name='grants_scar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.stockbattlescar'),
        ),
        migrations.AddField(
            model_name='trauma',
            name='name',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='asset',
            name='category',
            field=models.CharField(choices=[('PHYSICAL', 'Physical'), ('BACKGROUND', 'Background'), ('MENTAL', 'Mental'), ('RESTRICTED', 'Restricted')], default='PHYSICAL', max_length=50),
        ),
        migrations.AlterField(
            model_name='liability',
            name='category',
            field=models.CharField(choices=[('PHYSICAL', 'Physical'), ('BACKGROUND', 'Background'), ('MENTAL', 'Mental'), ('RESTRICTED', 'Restricted')], default='PHYSICAL', max_length=50),
        ),
        migrations.CreateModel(
            name='StockWorldElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=5000)),
                ('system', models.CharField(blank=True, max_length=1000)),
                ('type', models.CharField(choices=[('Condition', 'Condition'), ('Circumstance', 'Circumstance'), ('Trophy', 'Trophy'), ('Trauma', 'Trauma')], default='Condition', max_length=45)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.stockelementcategory')),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='grants_element',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.stockworldelement'),
        ),
        migrations.AddField(
            model_name='liability',
            name='grants_element',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.stockworldelement'),
        ),
    ]