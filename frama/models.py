from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser




class user_kyc_frama(models.Model):
    frama_user_id_no=models.ForeignKey("apps.profile",on_delete=models.CASCADE,null=True)    
    frama_Aadhar_card_no=models.IntegerField()
    frama_Pan_card_no=models.CharField(max_length=50)
    frama_Bank_Name=models.CharField(max_length=200)
    frama_Bank_account_number=models.IntegerField()
    frama_user_IFSC_code=models.CharField(max_length=200)
    frama_Bank_account_holder_name=models.CharField(max_length=200)
    frama_gst_no=models.CharField(max_length=50)
    frama_company_incorp_img=models.FileField(upload_to='frama incorporation', max_length=100)
    frama_profile_verification_video=models.FileField(upload_to='frama profile verification', max_length=100)
    frama_Aadhar_back_img=models.ImageField(upload_to='frama Adharcard back image/',blank=True,null=True)
    frama_Aaadhar_front_img=models.ImageField(upload_to='frama Adharcard front image/',blank=True,null=True)
    frama_Pan_card_img=models.ImageField(upload_to='frama Pancard image/',blank=True,null=True)


