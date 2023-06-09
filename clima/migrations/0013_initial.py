# Generated by Django 4.1.7 on 2023-04-06 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apps', '0063_user_kyc_dima'),
        ('clima', '0012_delete_user_kyc_clima'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_kyc_clima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clima_Aadhar_card_no', models.IntegerField()),
                ('clima_Pan_card_no', models.CharField(max_length=50)),
                ('clima_Bank_Name', models.CharField(max_length=200)),
                ('clima_Bank_account_number', models.IntegerField()),
                ('clima_user_IFSC_code', models.CharField(max_length=200)),
                ('clima_Bank_account_holder_name', models.CharField(max_length=200)),
                ('clima_gst_no', models.IntegerField(max_length=20)),
                ('cliam_company_incorp_img', models.FileField(upload_to='clima incorporation')),
                ('clima_profile_verification_video', models.FileField(upload_to='clima profile verification')),
                ('clima_Aadhar_back_img', models.ImageField(blank=True, null=True, upload_to='clima Adharcard back image/')),
                ('clima_Aaadhar_front_img', models.ImageField(blank=True, null=True, upload_to='clima Adharcard front image/')),
                ('clima_Pan_card_img', models.ImageField(blank=True, null=True, upload_to='clima Pancard image/')),
                ('clima_user_id_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.profile')),
            ],
        ),
    ]
