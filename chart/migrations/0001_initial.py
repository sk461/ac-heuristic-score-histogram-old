# Generated by Django 4.1.1 on 2022-12-06 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContestInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_name', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField()),
                ('finish_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment', models.CharField(max_length=30)),
                ('screen_name', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chart.contestinfo')),
            ],
        ),
        migrations.CreateModel(
            name='ResultInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('score', models.IntegerField(default=-1)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chart.taskinfo')),
            ],
        ),
    ]
