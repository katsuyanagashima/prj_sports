# Generated by Django 2.2.7 on 2020-02-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostCsv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=200)),
                ('player_name_formal', models.CharField(blank=True, max_length=200)),
                ('player_name_formal3', models.CharField(blank=True, max_length=200)),
                ('player_name_yomi', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tran_Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=1, verbose_name='区分')),
                ('KindOfData', models.CharField(max_length=1, verbose_name='データ種別')),
                ('DateOfSend', models.IntegerField(verbose_name='送信日')),
                ('DateOfRace1', models.CharField(max_length=8, verbose_name='競走年月日1')),
                ('SalesInfo1', models.CharField(max_length=1, verbose_name='場外発売情報1')),
                ('DateOfRace2', models.CharField(max_length=8, verbose_name='競走年月日2')),
                ('SalesInfo2', models.CharField(max_length=1, verbose_name='場外発売情報2')),
                ('DateOfRace3', models.CharField(max_length=8, verbose_name='競走年月日3')),
                ('SalesInfo3', models.CharField(max_length=1, verbose_name='場外発売情報3')),
            ],
        ),
    ]
