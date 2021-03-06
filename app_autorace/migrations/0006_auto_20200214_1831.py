# Generated by Django 2.1.4 on 2020-02-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_autorace', '0005_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='auto_schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(blank=True, max_length=1, verbose_name='区分')),
                ('kindofdata', models.CharField(blank=True, max_length=1, verbose_name='データ種別')),
                ('dateofsend', models.IntegerField(blank=True, null=True, verbose_name='送信日')),
                ('dateofrace1', models.CharField(blank=True, max_length=8, verbose_name='競争年月日1')),
                ('placeofrace1', models.CharField(blank=True, max_length=1, verbose_name='場外発売情報1')),
                ('place_code1_1', models.CharField(blank=True, max_length=1, verbose_name='場コード1_1')),
                ('numberofrace1_1', models.IntegerField(blank=True, null=True, verbose_name='レース数1_1')),
                ('place_code1_2', models.CharField(blank=True, max_length=1, verbose_name='場コード1_2')),
                ('numberofrace1_2', models.CharField(blank=True, max_length=2, null=True, verbose_name='レース数1_2')),
                ('place_code1_3', models.CharField(blank=True, max_length=1, verbose_name='場コード1_3')),
                ('numberofrace1_3', models.CharField(blank=True, max_length=2, null=True, verbose_name='レース数1_3')),
                ('place_code1_4', models.CharField(blank=True, max_length=1, verbose_name='場コード1_4')),
                ('numberofrace1_4', models.CharField(blank=True, max_length=2, null=True, verbose_name='レース数1_4')),
                ('place_code1_5', models.CharField(blank=True, max_length=1, verbose_name='場コード1_5')),
                ('numberofrace1_5', models.CharField(blank=True, max_length=2, null=True, verbose_name='レース数1_5')),
                ('place_code1_6', models.CharField(blank=True, max_length=1, verbose_name='場コード1_6')),
                ('numberofrace1_6', models.CharField(blank=True, max_length=2, null=True, verbose_name='レース数1_6')),
                ('dateofrace2', models.CharField(blank=True, max_length=8, verbose_name='競争年月日2')),
                ('placeofrace2', models.CharField(blank=True, max_length=1, verbose_name='場外発売情報2')),
                ('place_code2_1', models.CharField(blank=True, max_length=1, verbose_name='場コード2_1')),
                ('numberofrace2_1', models.CharField(blank=True, max_length=2, null=True, verbose_name='レース数2_1')),
                ('place_code2_2', models.CharField(blank=True, max_length=1, verbose_name='場コード2_2')),
                ('numberofrace2_2', models.CharField(blank=True, max_length=2, null=True, verbose_name='レース数2_2')),
                ('place_code2_3', models.CharField(blank=True, max_length=11, verbose_name='場コード2_3')),
                ('numberofrace2_3', models.CharField(blank=True, max_length=2, null=True, verbose_name='レース数2_3')),
                ('place_code2_4', models.CharField(blank=True, max_length=1, verbose_name='場コード2_4')),
                ('numberofrace2_4', models.CharField(blank=True, max_length=2, null=True, verbose_name='レース数2_4')),
                ('place_code2_5', models.CharField(blank=True, max_length=1, verbose_name='場コード2_5')),
                ('numberofrace2_5', models.CharField(blank=True, max_length=2, null=True, verbose_name='レース数2_5')),
                ('place_code2_6', models.CharField(blank=True, max_length=1, verbose_name='場コード2_6')),
                ('numberofrace2_6', models.CharField(blank=True, max_length=2, null=True, verbose_name='レース数2_6')),
                ('dateofrace3', models.CharField(blank=True, max_length=8, verbose_name='競争年月日3')),
                ('placeofrace3', models.CharField(blank=True, max_length=1, verbose_name='場外発売情報3')),
                ('place_code3_1', models.CharField(blank=True, max_length=1, verbose_name='場コード3_1')),
                ('numberofrace3_1', models.CharField(blank=True, max_length=2, null=True, verbose_name='レース数3_1')),
                ('place_code3_2', models.CharField(blank=True, max_length=1, verbose_name='場コード3_2')),
                ('numberofrace3_2', models.CharField(blank=True, max_length=2, null=True, verbose_name='レース数3_2')),
                ('place_code3_3', models.CharField(blank=True, max_length=1, verbose_name='場コード3_3')),
                ('numberofrace3_3', models.CharField(blank=True, max_length=2, null=True, verbose_name='レース数3_3')),
                ('place_code3_4', models.CharField(blank=True, max_length=1, verbose_name='場コード3_4')),
                ('numberofrace3_4', models.CharField(blank=True, max_length=2, null=True, verbose_name='レース数3_4')),
                ('place_code3_5', models.CharField(blank=True, max_length=1, verbose_name='場コード3_5')),
                ('numberofrace3_5', models.CharField(blank=True, max_length=2, null=True, verbose_name='レース数3_5')),
                ('place_code3_6', models.CharField(blank=True, max_length=1, verbose_name='場コード3_6')),
                ('numberofrace3_6', models.CharField(blank=True, max_length=2, null=True, verbose_name='レース数3_6')),
                ('prize30', models.CharField(blank=True, max_length=1, verbose_name='賞金上位30')),
            ],
            options={
                'verbose_name_plural': 'スケジュールレコード',
            },
        ),
        migrations.CreateModel(
            name='csvtest1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(blank=True, null=True, verbose_name='番号')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='名前')),
            ],
            options={
                'verbose_name_plural': 'CSVテスト１',
            },
        ),
        migrations.CreateModel(
            name='systemstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sys_status', models.IntegerField(blank=True, null=True, verbose_name='状態')),
                ('sys_display', models.CharField(blank=True, max_length=10, verbose_name='表示用')),
                ('sys_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name_plural': '運用状態',
            },
        ),
        migrations.DeleteModel(
            name='PostCsv',
        ),
        migrations.DeleteModel(
            name='Tran_Schedule',
        ),
    ]
