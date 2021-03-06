# Generated by Django 2.2 on 2020-11-24 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=50)),
                ('mailNum', models.EmailField(max_length=254)),
                ('phoneNum', models.IntegerField(default=0)),
                ('building', models.CharField(default='a', max_length=50)),
                ('classroomId', models.IntegerField(default=0)),
                ('repairType', models.CharField(default='a', max_length=50)),
                ('done', models.BooleanField(default=False)),
                ('manage', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
