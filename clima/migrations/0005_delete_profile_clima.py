# Generated by Django 4.1.7 on 2023-04-05 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clima', '0004_rename_user_profile_clima_user_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='profile_clima',
        ),
    ]
