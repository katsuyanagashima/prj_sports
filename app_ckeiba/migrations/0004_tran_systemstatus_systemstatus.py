# Generated by Django 2.1.4 on 2020-04-03 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_ckeiba', '0003_auto_20200402_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='tran_systemstatus',
            name='SystemStatus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app_ckeiba.Mst_Operationmode'),
        ),
    ]