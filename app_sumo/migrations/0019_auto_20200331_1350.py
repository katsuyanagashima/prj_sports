# Generated by Django 2.1.4 on 2020-03-31 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sumo', '0018_auto_20200329_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mst_kindofnewsml',
            name='NewsMLNo',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='NewsML種別コード'),
        ),
    ]
