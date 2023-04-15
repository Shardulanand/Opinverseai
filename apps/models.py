from django.db import models
from django.contrib.auth.models import User
from .utils import generate_ref_code
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser





class profile(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=True)
    code=models.CharField(max_length=12,blank=True)
    recommended:models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="ref_by")
    updated=models.DateTimeField( auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=50,default=None)
    last_name=models.CharField(max_length=50,default=None)
    designation=models.CharField(max_length=50,null=True)
    residence_state=models.CharField(max_length=50,null=True)
    mobile_number=models.IntegerField(null=True)
    Email_id=models.EmailField(max_length=254,null=True)
    skill1=models.CharField(max_length=50,null=True)
    skill2=models.CharField(max_length=50,null=True)
    skill3=models.CharField(max_length=50,null=True)
    skill4=models.CharField(max_length=50,null=True)
    skill5=models.CharField(max_length=50,null=True)
    Website_link=models.URLField(max_length=200,null=True)
    profile_img=models.ImageField(upload_to='profile image/',blank=True,null=True)

    def __str__(self):
        return f"{self.user.username}-{self.code}"

    def get_recommened_profile(self):
        pass

    def save(self, *args, **kwargs):
        if self.code=="":
            code=generate_ref_code()
            self.code=code
        super().save(*args, **kwargs)
    
    
class user_kyc_dima(models.Model):
    user_id_no=models.CharField(max_length=50)    
    Aadhar_card_no=models.IntegerField()
    Pan_card_no=models.CharField(max_length=50)
    Bank_Name=models.CharField(max_length=200)
    Bank_account_number=models.IntegerField()
    user_IFSC_code=models.CharField(max_length=200)
    Bank_account_holder_name=models.CharField(max_length=200)
    profile_verification_video=models.FileField(upload_to='Profile Verification video', max_length=100)
    Aadhar_back_img=models.ImageField(upload_to='Adharcard back image/',blank=True,null=True)
    Aaadhar_front_img=models.ImageField(upload_to='Adharcard front image/',blank=True,null=True)
    Pan_card_img=models.ImageField(upload_to='Pancard image/',blank=True,null=True)













