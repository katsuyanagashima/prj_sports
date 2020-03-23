# Generated by Django 2.1.4 on 2020-03-20 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sumo', '0026_mst_kindofnewsml'),
    ]

    operations = [
        migrations.AddField(
            model_name='mst_kindofnewsml',
            name='Content_code',
            field=models.IntegerField(blank=True, null=True, verbose_name='電文種別コード'),
        ),
        migrations.AlterField(
            model_name='mst_kindofnewsml',
            name='NewsMLNo',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='NewsML種別コード'),
        ),
    ]