from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from apps.models import *
from clima.models import *
from admin_panel.models import *
from django.contrib.auth.decorators import login_required
from apps.forms import *
from django.core.mail import send_mail


app_name="apps"

def admin_panel(request):
    return render(request,'admin_panel/admin_dashboard.html')

def userlist_dima(request):
    profileinst = profile.objects.all()                     
    context={
        'profileinst':profileinst,
    }
    return render(request,'admin_panel/userslist_dima.html',context)

def kyclist_dima(request):
    kycinst=user_kyc_dima.objects.all()
    context={
        'kycinst':kycinst,
    }
    return render(request,'admin_panel/kyclist_dima.html',context)

def userlist_clima(request):
    profileinst = profile.objects.all()                     
    context={
        'profileinst':profileinst,
    }
    return render(request,'admin_panel/userlists_clima.html',context)

def kyclist_clima(request):
    kycinstclima=user_kyc_clima.objects.all()
    context={
        'kycinstclima':kycinstclima,
    }
    return render(request,'admin_panel/kyclist_clima.html',context)