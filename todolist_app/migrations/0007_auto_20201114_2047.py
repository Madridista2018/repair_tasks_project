# Generated by Django 2.2 on 2020-11-14 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0006_auto_20201114_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='addTime',
            field=models.IntegerField(default=1),
        ),
    ]
