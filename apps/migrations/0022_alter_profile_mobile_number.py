# Generated by Django 4.1.7 on 2023-04-01 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0021_profile_skill2_profile_skill3_profile_skill4_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile_number',
            field=models.BigIntegerField(max_length=12, null=True),
        ),
    ]
