from django.urls import path
from admin_panel.views import *
app_name = "admin_panel"


urlpatterns = [
    path("admin_panel/",admin_panel,name='admin_panelurls'),
    path("userlist_dima/",userlist_dima,name='userlist_dimaurls'),
    path("kyclist_dima/",kyclist_dima,name='kyclist_dimaurls'),
    path("userlist_clima/",userlist_clima,name='userlist_climaurls'),
    path("kyclist_clima/",kyclist_clima,name='kyclist_climaurls'),
]