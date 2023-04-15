from django import forms
from django.contrib.auth.models import *
from frama.models import *


class framaForm(forms.ModelForm):
       class Meta:
              model=user_kyc_frama
              fields=['frama_Aadhar_card_no','frama_Pan_card_no','frama_Bank_Name','frama_Bank_account_number','frama_user_IFSC_code','frama_Bank_account_holder_name','frama_gst_no','frama_company_incorp_img','frama_profile_verification_video','frama_Aadhar_back_img','frama_Aaadhar_front_img','frama_Pan_card_img']

