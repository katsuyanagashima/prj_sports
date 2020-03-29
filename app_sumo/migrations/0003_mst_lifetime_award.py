# Generated by Django 2.1.4 on 2020-03-28 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_sumo', '0002_auto_20200328_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mst_Lifetime_award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Award_category_kanji', models.CharField(max_length=10, verbose_name='受賞名漢字')),
                ('Award_category_kana', models.CharField(blank=True, max_length=20, verbose_name='受賞名かな')),
                ('Award_category_name1', models.CharField(blank=True, max_length=10, verbose_name='名称１')),
                ('Award_category_name2', models.CharField(blank=True, max_length=10, verbose_name='名称２')),
                ('Award_category_name3', models.CharField(blank=True, max_length=10, verbose_name='名称３')),
                ('Award_category_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sumo.Mst_Award_category')),
                ('Rikishi_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sumo.Mst_Rikishi')),
            ],
            options={
                'verbose_name_plural': '生涯受賞回数マスタ',
            },
        ),
    ]
