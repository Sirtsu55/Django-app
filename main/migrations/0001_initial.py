# Generated by Django 3.0.8 on 2020-07-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('APP_NAME', models.CharField(max_length=100)),
                ('APP_PASS', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
