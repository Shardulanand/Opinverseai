# Generated by Django 4.1.7 on 2023-04-02 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0031_profile_email_id_profile_website_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile_number',
            field=models.IntegerField(null=True),
        ),
    ]
