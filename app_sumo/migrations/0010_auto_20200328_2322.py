# Generated by Django 2.1.4 on 2020-03-28 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_sumo', '0009_auto_20200328_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nml_01',
            name='BashoCount',
        ),
        migrations.RemoveField(
            model_name='nml_01',
            name='Event_date',
        ),
        migrations.RemoveField(
            model_name='nml_01',
            name='RikishiId',
        ),
        migrations.DeleteModel(
            name='NML_01',
        ),
    ]
