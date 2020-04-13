# Generated by Django 2.1.4 on 2020-04-10 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mst_Accident_reason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Accident_reason_code', models.IntegerField(verbose_name='事故理由コード')),
                ('Accident_reason_name', models.CharField(max_length=15, verbose_name='事故理由名称')),
            ],
            options={
                'verbose_name_plural': '事故理由マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Accident_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Accident_type_code', models.IntegerField(verbose_name='事故種類コード')),
                ('Accident_type_name', models.CharField(max_length=15, verbose_name='事故種類名称')),
                ('Accident_type_priority', models.IntegerField(blank=True, verbose_name='優先順位')),
            ],
            options={
                'verbose_name_plural': '事故種類マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Affiliation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Affiliation_code', models.IntegerField(verbose_name='所属場コード')),
                ('Affiliation_name', models.CharField(max_length=10, verbose_name='所属場名称（正式名）')),
                ('Affiliation_1char', models.CharField(max_length=1, verbose_name='所属場名称（1字）')),
            ],
            options={
                'verbose_name_plural': '所属場マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Baba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Baba_code', models.IntegerField(verbose_name='馬場状態コード')),
                ('Baba_name', models.CharField(max_length=5, verbose_name='馬場状態名称')),
            ],
            options={
                'verbose_name_plural': '馬場状態マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Bigmargin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bigmargin_code', models.IntegerField(verbose_name='差コード')),
                ('Bigmargin_name', models.CharField(max_length=5, verbose_name='差名称')),
                ('Bigmargin_display_name', models.CharField(blank=True, max_length=5, verbose_name='画面表示用名称')),
            ],
            options={
                'verbose_name_plural': '差マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Breed_age',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Breed_age_code', models.IntegerField(verbose_name='品種年齢区分')),
                ('Breed_age_name', models.CharField(max_length=10, verbose_name='競走種別用名称')),
                ('Breed_age_age_name', models.CharField(max_length=10, verbose_name='馬齢条件用名称')),
                ('Breed_age_breed_name', models.CharField(max_length=10, verbose_name='品種年齢名称')),
            ],
            options={
                'verbose_name_plural': '品種年齢区分マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_code', models.IntegerField(verbose_name='配信社コード')),
                ('Company_name', models.CharField(max_length=5, verbose_name='配信社名称')),
                ('Company_block', models.BooleanField(verbose_name='ブロック指定フラグ')),
                ('Company_yobi', models.CharField(blank=True, max_length=30, null=True, verbose_name='予備')),
            ],
            options={
                'verbose_name_plural': '【配信系】配信社マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_code', models.IntegerField(verbose_name='コース区分コード')),
                ('Course_name', models.CharField(max_length=15, verbose_name='コース区分名称')),
            ],
            options={
                'verbose_name_plural': 'コース区分マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Grade_code', models.IntegerField(verbose_name='グレード区分')),
                ('Grade_name', models.CharField(max_length=5, verbose_name='グレード名称')),
            ],
            options={
                'verbose_name_plural': 'グレードマスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Haishin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Haishin_racekaku', models.CharField(max_length=5, verbose_name='レース格')),
                ('Haishin_haishinsaki', models.CharField(max_length=5, verbose_name='配信先')),
                ('Haishin_yobi', models.CharField(blank=True, max_length=30, null=True, verbose_name='予備')),
            ],
            options={
                'verbose_name_plural': '【配信系】通常配信先マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Haishin_gentei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Haishin_gentei_start', models.CharField(max_length=20, verbose_name='開始日時')),
                ('Haishin_gentei_end', models.CharField(max_length=20, verbose_name='終了日時')),
                ('Haishin_gentei_start_race', models.CharField(max_length=5, verbose_name='開始R')),
                ('Haishin_gentei_end_race', models.CharField(max_length=5, verbose_name='終了R')),
                ('Haishin_gentei_file_name', models.CharField(max_length=15, verbose_name='ファイル名')),
                ('Haishin_yobi', models.CharField(blank=True, max_length=30, null=True, verbose_name='予備')),
                ('Company_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ckeiba.Mst_Company', verbose_name='配信社コード')),
            ],
            options={
                'verbose_name_plural': '【配信系】期間限定配信先マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Handicap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Handicap_code', models.IntegerField(verbose_name='負担重量区分コード')),
                ('Handicap_name', models.CharField(max_length=5, verbose_name='負担重量区分名称')),
            ],
            options={
                'verbose_name_plural': '負担重量区分マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Honjitu_Shikou',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Honjitu_Shikou_date', models.DateField(verbose_name='本日施行情報')),
            ],
            options={
                'verbose_name_plural': '【スケジュール系】本日施行情報',
            },
        ),
        migrations.CreateModel(
            name='Mst_Jockey_change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jockey_change_code', models.IntegerField(verbose_name='騎手変更理由コード')),
                ('Jockey_change_name', models.CharField(max_length=25, verbose_name='騎手変更理由名称')),
            ],
            options={
                'verbose_name_plural': '騎手変更理由マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Jou',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jou_code', models.IntegerField(verbose_name='競馬場コード')),
                ('Jou_name', models.CharField(max_length=20, verbose_name='正式名')),
                ('Jou_seisekiA', models.CharField(max_length=5, verbose_name='成績Ａ用')),
                ('Jou_3char', models.CharField(max_length=3, verbose_name='３字略称')),
                ('Jou_banei', models.BooleanField(verbose_name='ばんえいフラグ')),
                ('Jou_1corner', models.CharField(blank=True, max_length=5, null=True, verbose_name='１コーナー名称')),
                ('Jou_2corner', models.CharField(blank=True, max_length=5, null=True, verbose_name='２コーナー名称')),
                ('Jou_3corner', models.CharField(blank=True, max_length=5, null=True, verbose_name='３コーナー名称')),
                ('Jou_4corner', models.CharField(blank=True, max_length=5, null=True, verbose_name='４コーナー名称')),
            ],
            options={
                'verbose_name_plural': '競馬場マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Kaisai_Hiwari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Kaisai_Hiwari_date', models.DateField(verbose_name='開催日割')),
            ],
            options={
                'verbose_name_plural': '【スケジュール系】開催日割',
            },
        ),
        migrations.CreateModel(
            name='Mst_Margin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Margin_code', models.IntegerField(verbose_name='着差コード')),
                ('Margin_name', models.CharField(max_length=5, verbose_name='着差名称')),
            ],
            options={
                'verbose_name_plural': '着差マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Matter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Matter_code', models.IntegerField(verbose_name='事象コード')),
                ('Matter_name', models.CharField(max_length=15, verbose_name='事象名称')),
            ],
            options={
                'verbose_name_plural': '事象マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_MixJRA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MixJRA_code', models.IntegerField(verbose_name='中央交流区コード')),
                ('MixJRA_name', models.CharField(max_length=15, verbose_name='交流区分名称')),
                ('MixJRA_1char', models.IntegerField(verbose_name='配信区分コード')),
            ],
            options={
                'verbose_name_plural': '中央交流区マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Night_race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Night_race_code', models.BooleanField(verbose_name='ナイター区分コード')),
                ('Night_race_name', models.CharField(max_length=5, verbose_name='ナイター区分名称')),
            ],
            options={
                'verbose_name_plural': 'ナイター区分マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Operationmode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Operationmode_code', models.IntegerField(verbose_name='運用モード')),
                ('Operationmode_name', models.CharField(max_length=15, verbose_name='運用モード表記')),
            ],
            options={
                'verbose_name_plural': '#運用管理',
            },
        ),
        migrations.CreateModel(
            name='Mst_Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Printer_kei', models.IntegerField(verbose_name='系')),
                ('Printer_output', models.CharField(max_length=5, verbose_name='出力系')),
                ('Haishin_yobi', models.CharField(blank=True, max_length=30, null=True, verbose_name='予備')),
            ],
            options={
                'verbose_name_plural': '【配信系】プリンタ出力先マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Race_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Race_type_code', models.IntegerField(verbose_name='競走種類コード')),
                ('Race_type_name', models.CharField(max_length=15, verbose_name='競走種類名称')),
                ('Race_type_deliverytype', models.IntegerField(verbose_name='配信区分')),
            ],
            options={
                'verbose_name_plural': '競走種類マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Rotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rotation_code', models.IntegerField(verbose_name='回り区分コード')),
                ('Rotation_name', models.CharField(max_length=5, verbose_name='回り区分名称')),
            ],
            options={
                'verbose_name_plural': '回り区分マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Sex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sex_code', models.IntegerField(verbose_name='性別コード')),
                ('Sex_name', models.CharField(max_length=2, verbose_name='性別名称')),
                ('Sex_sub', models.CharField(blank=True, max_length=5, verbose_name='性別備考')),
            ],
            options={
                'verbose_name_plural': '性別マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Target_person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Target_person_code', models.IntegerField(verbose_name='対象者コード')),
                ('Target_person_name', models.CharField(max_length=15, verbose_name='対象者名称')),
            ],
            options={
                'verbose_name_plural': '対象者マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Turf_dirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Turf_dirt_code', models.IntegerField(verbose_name='芝・ダート区分コード')),
                ('Turf_dirt_name', models.CharField(max_length=15, verbose_name='芝区分名称')),
            ],
            options={
                'verbose_name_plural': '芝・ダート区分マスタ',
            },
        ),
        migrations.CreateModel(
            name='Mst_Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Weather_code', models.IntegerField(verbose_name='天候コード')),
                ('Weather_name', models.CharField(max_length=5, verbose_name='天候名称')),
            ],
            options={
                'verbose_name_plural': '天候マスタ',
            },
        ),
        migrations.CreateModel(
            name='Tran_Systemstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unyou_date', models.DateField(verbose_name='運用日')),
                ('SystemStatus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_ckeiba.Mst_Operationmode')),
            ],
            options={
                'verbose_name_plural': '#システム状態',
            },
        ),
        migrations.AddField(
            model_name='mst_haishin_gentei',
            name='Jou_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ckeiba.Mst_Jou', verbose_name='競馬場コード'),
        ),
        migrations.AddField(
            model_name='mst_haishin',
            name='Jou_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ckeiba.Mst_Jou', verbose_name='競馬場コード'),
        ),
    ]
