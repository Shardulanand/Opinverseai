# Generated by Django 4.1.7 on 2023-03-30 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_remove_user_refrence_user_id_delete_masteruser_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='masteruser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('masterid', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('email_address', models.CharField(max_length=150)),
            ],
        ),
    ]
