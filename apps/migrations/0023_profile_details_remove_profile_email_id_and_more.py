# Generated by Django 4.1.7 on 2023-04-01 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0022_alter_profile_mobile_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=50, null=True)),
                ('residence_state', models.CharField(max_length=50, null=True)),
                ('mobile_number', models.BigIntegerField(max_length=12, null=True)),
                ('Email_id', models.EmailField(max_length=254, null=True)),
                ('skill1', models.CharField(max_length=50, null=True)),
                ('skill2', models.CharField(max_length=50, null=True)),
                ('skill3', models.CharField(max_length=50, null=True)),
                ('skill4', models.CharField(max_length=50, null=True)),
                ('skill5', models.CharField(max_length=50, null=True)),
                ('Website_link', models.URLField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Email_id',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Website_link',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='residence_state',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='skill1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='skill2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='skill3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='skill4',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='skill5',
        ),
    ]