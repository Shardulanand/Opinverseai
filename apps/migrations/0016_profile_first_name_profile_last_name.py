# Generated by Django 4.1.7 on 2023-04-01 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0015_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
