from django.urls import path
from frama.views import *
app_name = "frama"


urlpatterns = [
    path('Frama_Login/',mylogin_frama,name='mylogin_framaurls'),
    path('frama_index/',frama_index,name='frama_indexurls'),
    path('frama_Profile/',frama_Profile,name='frama_Profileurls'),
    path('mylogout_frama/',mylogout_frama,name='mylogout_framaurls'),
    path('frama_userprofile_setting/',frama_userprofile_setting,name='frama_userprofile_settingurls'),
    path('kyc_frama/',kyc_frama,name='kyc_framaurls'),
    path('frama_activities/',frama_activities,name='frama_activitiesurls'),
    path('frama_qualification/',frama_qualification,name='frama_qualificationurls'),
    path('frama_documents/',frama_documents,name='frama_documentsurls'),
    path('frama_billingpayments/',frama_billingpayments,name='frama_billingpaymentsurls'),
    path('frama_User_Subscription/',frama_User_Subscription,name='frama_User_Subscriptionurls'),
    path('calender_frama/',calender_frama,name='calender_framaurls'),
    path('frama_gig_all/',frama_gig_all,name='frama_gig_allurls'),
    path('frama_gig_new/',frama_gig_new,name='frama_gig_newurls'),
    path('frama_gig_previous/',frama_gig_previous,name='frama_gig_previousurls'),
    path('frama_gig_feedback/',frama_gig_feedback,name='frama_gig_feedbackurls'),
    path('frama_task/',frama_task,name='frama_taskurls'),
    path('frama_brands/',frama_brands,name='frama_brandsurls'),
    path('frama_projects/',frama_projects,name='frama_projectsurls'),
    path('frama_CRM_Contacts/',frama_CRM_Contacts,name='frama_CRM_Contactsurls'),
    path('frama_CRM_companies/',frama_CRM_companies,name='frama_CRM_companiesurls'),
    path('frama_CRM_deals/',frama_CRM_deals,name='frama_CRM_dealsurls'),
    path('frama_CRM_leads/',frama_CRM_leads,name='frama_CRM_leadsurls'),
    path('frama_supportticket_create/',frama_supportticket_create,name='frama_supportticket_createurls'),
    path('frama_supportticket_details/',frama_supportticket_details,name='frama_supportticket_detailsurls'),
    path('frama_supportticket_history/',frama_supportticket_history,name='frama_supportticket_historyurls'),
    
]