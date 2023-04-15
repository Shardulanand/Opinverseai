from django.contrib import admin
from frama.models import *




@admin.register(user_kyc_frama)
class user_kyc_dima_admin(admin.ModelAdmin):
     list_display=('frama_user_id_no','frama_Aadhar_card_no','frama_Pan_card_no','frama_Bank_Name','frama_Bank_account_number','frama_user_IFSC_code','frama_Bank_account_holder_name','frama_gst_no','frama_company_incorp_img','frama_profile_verification_video','frama_Aadhar_back_img','frama_Aaadhar_front_img','frama_Pan_card_img')
