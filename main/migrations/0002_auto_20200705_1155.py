# Generated by Django 3.0.8 on 2020-07-05 08:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citle', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_added', models.DateTimeField(default=datetime.datetime(2020, 7, 5, 11, 55, 31, 732121), verbose_name='date published')),
            ],
        ),
        migrations.DeleteModel(
            name='AppData',
        ),
    ]