# Generated by Django 3.0.4 on 2020-03-24 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0025_filmdescription_operator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmdescription',
            name='operator',
            field=models.CharField(max_length=150),
        ),
    ]
