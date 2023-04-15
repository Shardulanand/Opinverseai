# Generated by Django 4.1.7 on 2023-03-14 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='revenue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('level', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('package', models.CharField(max_length=50)),
                ('referrer', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('date', models.DateField(max_length=8)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
