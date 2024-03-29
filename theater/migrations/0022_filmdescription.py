# Generated by Django 3.0.4 on 2020-03-24 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0021_auto_20200324_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=20)),
                ('genre', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=150)),
                ('director', models.CharField(max_length=150)),
                ('screenwriter', models.CharField(max_length=150)),
                ('producer', models.CharField(max_length=150)),
                ('composer', models.CharField(max_length=150)),
                ('budget', models.IntegerField()),
                ('duration', models.CharField(max_length=150)),
                ('age', models.CharField(max_length=10)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theater.Film')),
            ],
        ),
    ]
