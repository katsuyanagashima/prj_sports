# Generated by Django 2.2.6 on 2019-11-03 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sumo', '0005_auto_20191103_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winloss', models.CharField(max_length=200)),
                ('win', models.CharField(max_length=200)),
                ('loss', models.CharField(max_length=200)),
                ('tie', models.CharField(max_length=200)),
                ('absence', models.CharField(max_length=200)),
            ],
        ),
    ]
