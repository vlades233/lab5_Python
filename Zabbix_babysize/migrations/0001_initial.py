# Generated by Django 2.2.7 on 2019-11-26 11:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zabbix_babysize',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='this is unique ID ZULUL', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('time', models.TimeField(auto_now=True)),
                ('date', models.DateField(auto_now=True)),
                ('ntype', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('gtype', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=100)),
                ('locate', models.CharField(max_length=100)),
            ],
        ),
    ]
