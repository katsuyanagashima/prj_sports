# Generated by Django 2.2.6 on 2019-11-03 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sumo', '0002_player_player_name_formal'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='player_name_formal3',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='player',
            name='player_name_yomi',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]