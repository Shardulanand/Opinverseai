# Generated by Django 4.1.7 on 2023-04-05 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clima', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile_clima',
            old_name='user_clima',
            new_name='user',
        ),
    ]