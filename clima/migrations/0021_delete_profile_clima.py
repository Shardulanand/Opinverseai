# Generated by Django 4.1.7 on 2023-04-06 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clima', '0020_rename_user_clima_profile_clima_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='profile_clima',
        ),
    ]
