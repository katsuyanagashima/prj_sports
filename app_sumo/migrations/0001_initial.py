# Generated by Django 2.2.6 on 2019-11-02 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eventinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taikai_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=200)),
                ('winloss', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Waza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waza_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('outcome1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rikishi_1', to='app_sumo.Outcome')),
                ('outcome2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rikishi_2', to='app_sumo.Outcome')),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rikishi_1', to='app_sumo.Player')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rikishi_2', to='app_sumo.Player')),
                ('waza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sumo.Waza')),
            ],
        ),
    ]
