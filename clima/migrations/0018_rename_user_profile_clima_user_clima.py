# Generated by Django 4.1.7 on 2023-04-06 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clima', '0017_profile_clima'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile_clima',
            old_name='user',
            new_name='user_clima',
        ),
    ]