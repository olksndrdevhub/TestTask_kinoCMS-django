# Generated by Django 3.0.4 on 2020-03-24 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0014_auto_20200324_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='show_now_duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
