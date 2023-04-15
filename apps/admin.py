from django.contrib import admin
from apps.models import *
from django.contrib import admin
from .models import *
from .forms import *


admin.site.register(profile)






@admin.register(user_kyc_dima)
class user_kyc_dima_admin(admin.ModelAdmin):
     list_display=('user_id_no','Aadhar_card_no','Pan_card_no','Bank_Name','Bank_account_number','user_IFSC_code','Bank_account_holder_name','profile_verification_video','Aadhar_back_img','Aaadhar_front_img','Pan_card_img')







