from django.contrib import admin
from clima.models import *




@admin.register(user_kyc_clima)
class user_kyc_dima_admin(admin.ModelAdmin):
     list_display=('clima_user_id_no','clima_Aadhar_card_no','clima_Pan_card_no','clima_Bank_Name','clima_Bank_account_number','clima_user_IFSC_code','clima_Bank_account_holder_name','clima_gst_no','clima_company_incorp_img','clima_profile_verification_video','clima_Aadhar_back_img','clima_Aaadhar_front_img','clima_Pan_card_img')
