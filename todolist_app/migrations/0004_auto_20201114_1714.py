# Generated by Django 2.2 on 2020-11-14 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0003_auto_20201113_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='mail_num',
            field=models.EmailField(max_length=254),
        ),
    ]