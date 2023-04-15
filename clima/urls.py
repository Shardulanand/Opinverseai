from django.urls import path
from clima.views import *
app_name = "clima"


urlpatterns = [
    path('Clima_Login',mylogin_clima,name="Clima_Loginurls"),
    path('clima_index',clima_index,name="clima_indexurls"),
    path('logout/',mylogout_clima,name='mylogouturl_clima'),
    path('clima_userprofile',clima_userprofile,name="clima_userprofileurls"),
    path('Profile_setting_clima',Profile_setting_clima,name="Profile_setting_climaurls"),
    path('kyc_clima/',kyc_clima,name="kyc_climaurls"),
    path('clima_activites/',clima_activites, name="clima_activitesurls"),
    path('qualification_clima/',qualification_clima, name="qualification_climaurls"),
    path('documents_clima/',documents_clima, name="documents_climaurls"),
    path('billingpayments_clima/',billingpayments_clima, name="billingpayments_climaurls"),
    path('clima_wallet_dashboard/',clima_wallet_dashboard, name="clima_wallet_dashboardurls"),
    path('clima_wallet_history/',clima_wallet_history, name="clima_wallet_historyurls"),
    path('clima_User_Subscription/',clima_User_Subscription, name="clima_User_Subscriptionurls"),
    path('calender_clima/',calender_clima, name="calender_climaurls"),
    path('clima_CRM_Contacts/',clima_CRM_Contacts, name="clima_CRM_Contactsurls"),
    path('clima_CRM_companies/',clima_CRM_companies, name="clima_CRM_companiesurls"),
    path('clima_CRM_deals/',clima_CRM_deals, name="clima_CRM_dealsurls"),
    path('clima_CRM_leads/',clima_CRM_leads, name="clima_CRM_leadsurls"),
    path('clima_task/',clima_task, name="clima_taskurls"),
    path('clima_brands/',clima_brands, name="clima_brandsurls"),
    path('clima_projects/',clima_projects, name="clima_projectsurls"),
    path('clima_supportticket_create/',clima_supportticket_create, name="clima_supportticket_createurls"),
    path('clima_supportticket_details/',clima_supportticket_details, name="clima_supportticket_detailsurls"),
    path('clima_supportticket_history/',clima_supportticket_history, name="clima_supportticket_historyurls"),
    path('gig_all/',gig_all, name="gig_allurls"),
    path('gig_new/',gig_new, name="gig_newurls"),
    path('gig_previous/',gig_previous, name="gig_previousurls"),
    path('gig_feedback/',gig_feedback, name="gig_feedbackurls"),
]