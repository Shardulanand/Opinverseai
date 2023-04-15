from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser




class user_kyc_clima(models.Model):
    clima_user_id_no=models.CharField(max_length=50)    
    clima_Aadhar_card_no=models.IntegerField()
    clima_Pan_card_no=models.CharField(max_length=50)
    clima_Bank_Name=models.CharField(max_length=200)
    clima_Bank_account_number=models.IntegerField()
    clima_user_IFSC_code=models.CharField(max_length=200)
    clima_Bank_account_holder_name=models.CharField(max_length=200)
    clima_gst_no=models.CharField(max_length=50)
    clima_company_incorp_img=models.FileField(upload_to='clima incorporation', max_length=100)
    clima_profile_verification_video=models.FileField(upload_to='clima profile verification', max_length=100)
    clima_Aadhar_back_img=models.ImageField(upload_to='clima Adharcard back image/',blank=True,null=True)
    clima_Aaadhar_front_img=models.ImageField(upload_to='clima Adharcard front image/',blank=True,null=True)
    clima_Pan_card_img=models.ImageField(upload_to='clima Pancard image/',blank=True,null=True)


