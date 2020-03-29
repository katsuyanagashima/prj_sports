# Generated by Django 2.1.4 on 2020-03-28 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_sumo', '0007_auto_20200328_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='NML_01',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EntryNo', models.IntegerField(blank=True, null=True, verbose_name='登録順位')),
                ('BashoCount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sumo.Mst_Lifetime_result')),
            ],
            options={
                'verbose_name_plural': '*NewsML 01：新番付資料',
            },
        ),
        migrations.CreateModel(
            name='Tran_Systemstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_date', models.IntegerField(blank=True, null=True, verbose_name='開催年月')),
                ('Frist_date', models.DateField(verbose_name='初日年月日')),
                ('Banzuke_date', models.DateField(verbose_name='番付発表日')),
                ('Age_calcu_reference_date', models.DateField(verbose_name='年齢算出基準日')),
                ('CurrentBasho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sumo.Mst_Basho')),
                ('MatchDate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='app_sumo.Mst_Nichime')),
                ('SystemStatus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_sumo.Mst_Operationmode')),
                ('TorikumiDate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='torikumi', to='app_sumo.Mst_Nichime')),
            ],
            options={
                'verbose_name_plural': '#システム状態',
            },
        ),
        migrations.AddField(
            model_name='nml_01',
            name='Event_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sumo.Tran_Systemstatus'),
        ),
        migrations.AddField(
            model_name='nml_01',
            name='RikishiId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sumo.Mst_Nichime'),
        ),
    ]
