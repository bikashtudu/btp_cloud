# Generated by Django 2.0.5 on 2018-11-06 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SLAStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('vm', models.CharField(max_length=10)),
                ('timestamp', models.CharField(max_length=25)),
                ('sla', models.CharField(max_length=40)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
