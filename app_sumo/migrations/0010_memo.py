# Generated by Django 2.2.7 on 2019-11-07 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sumo', '0009_auto_20191103_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=200)),
            ],
        ),
    ]
