# Generated by Django 4.1.7 on 2023-04-04 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0040_delete_user_kyc_dima'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_kyc_dima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]