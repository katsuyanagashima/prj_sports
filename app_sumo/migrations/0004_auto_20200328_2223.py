# Generated by Django 2.1.4 on 2020-03-28 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_sumo', '0003_mst_lifetime_award'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mst_lifetime_award',
            name='Award_category_code',
        ),
        migrations.RemoveField(
            model_name='mst_lifetime_award',
            name='Rikishi_code',
        ),
        migrations.DeleteModel(
            name='Mst_Lifetime_award',
        ),
    ]
