# Generated by Django 3.0.4 on 2020-03-24 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0022_filmdescription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filmdescription',
            old_name='producer',
            new_name='operator',
        ),
    ]
