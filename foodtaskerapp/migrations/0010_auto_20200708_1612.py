# Generated by Django 3.0.8 on 2020-07-08 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0009_auto_20200708_1149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='restautant',
            new_name='restaurant',
        ),
    ]
