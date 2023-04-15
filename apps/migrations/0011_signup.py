# Generated by Django 4.1.7 on 2023-03-30 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0010_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('refrence_id', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(max_length=12)),
                ('password_1', models.CharField(max_length=15)),
            ],
        ),
    ]