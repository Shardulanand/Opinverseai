# Generated by Django 4.1.7 on 2023-04-04 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0050_delete_user_kyc_dima'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_kyc_dima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aadhar_card_no', models.IntegerField()),
                ('Pan_card_no', models.CharField(max_length=200)),
                ('Bank_Name', models.CharField(max_length=200)),
                ('user_id_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.profile')),
            ],
        ),
    ]
