# Generated by Django 2.2 on 2020-11-14 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0010_auto_20201114_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='addDate',
        ),
    ]