# Generated by Django 4.1.7 on 2023-03-15 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Digitalmarketingrevenue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project', models.CharField(max_length=150)),
                ('task', models.CharField(max_length=5000)),
                ('ovcash', models.IntegerField()),
                ('client', models.CharField(max_length=550)),
                ('campaignteam', models.CharField(max_length=550)),
                ('duedate', models.DateField(max_length=8)),
                ('status', models.CharField(max_length=550)),
                ('priority', models.CharField(max_length=550)),
            ],
        ),
    ]
