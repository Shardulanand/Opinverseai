# Generated by Django 4.1.7 on 2023-04-04 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0043_user_kyc_dima'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_kyc_dima',
            name='Bank_Name',
        ),
        migrations.RemoveField(
            model_name='user_kyc_dima',
            name='Bank_account_holder_name',
        ),
        migrations.RemoveField(
            model_name='user_kyc_dima',
            name='Bank_account_number',
        ),
        migrations.RemoveField(
            model_name='user_kyc_dima',
            name='Pan_card_no',
        ),
        migrations.RemoveField(
            model_name='user_kyc_dima',
            name='user_IFSC_code',
        ),
    ]