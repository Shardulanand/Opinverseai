from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import *
from .models import *


class DimaForm(forms.ModelForm):
   class Meta:
       model=user_kyc_dima
       fields=['user_id_no','Aadhar_card_no','Pan_card_no','Bank_Name','Bank_account_number','user_IFSC_code','Bank_account_holder_name','profile_verification_video','Aadhar_back_img','Aaadhar_front_img','Pan_card_img']























# from django import forms

# class DimaForm(forms.ModelForm):
#     class Meta:
#         model = user_kyc_dima
#         fields = ['name', 'message']
