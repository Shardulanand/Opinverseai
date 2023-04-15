from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import *
from clima.models import *


# class climaForm(forms.ModelForm):
#        class Meta:
#        model=user_kyc_clima
#        fields=['clima_Aadhar_card_no','clima_Pan_card_no','clima_Bank_Name','clima_Bank_account_number','clima_user_IFSC_code','clima_Bank_account_holder_name','clima_profile_verification_video','clima_Aadhar_back_img','clima_Aaadhar_front_img','clima_Pan_card_img']


class climaForm(forms.ModelForm):
   class Meta:
       model=user_kyc_clima
       fields=['clima_user_id_no','clima_Aadhar_card_no','clima_Pan_card_no','clima_Bank_Name','clima_Bank_account_number','clima_user_IFSC_code','clima_Bank_account_holder_name','clima_gst_no','clima_company_incorp_img','clima_profile_verification_video','clima_Aadhar_back_img','clima_Aaadhar_front_img','clima_Pan_card_img']

