# Generated by Django 2.0.7 on 2018-07-10 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diao', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='creat_time',
            new_name='create_time',
        ),
    ]
