# Generated by Django 4.1.7 on 2023-04-02 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0030_remove_profile_email_id_remove_profile_website_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Email_id',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Website_link',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='designation',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile_number',
            field=models.IntegerField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='profile image/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='residence_state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='skill1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='skill2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='skill3',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='skill4',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='skill5',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
