# Generated by Django 2.1.4 on 2020-03-29 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_sumo', '0011_nml_01'),
    ]

    operations = [
        migrations.CreateModel(
            name='NML_00_comm_incontent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Competition', models.ForeignKey(db_column='CurrentBasho', on_delete=django.db.models.deletion.CASCADE, related_name='bash', to='app_sumo.Tran_Systemstatus')),
                ('CompetitionDay', models.ForeignKey(db_column='TorikumiDate', on_delete=django.db.models.deletion.CASCADE, related_name='nichime', to='app_sumo.Tran_Systemstatus')),
                ('YearMonth', models.ForeignKey(db_column='Event_date', on_delete=django.db.models.deletion.CASCADE, related_name='date', to='app_sumo.Tran_Systemstatus')),
            ],
            options={
                'verbose_name_plural': '*NewsML 00：共通・内容情報部）',
            },
        ),
    ]
