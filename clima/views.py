
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from clima.models import *
from django.contrib.auth.decorators import login_required
from apps.forms import *
from django.core.mail import send_mail
from clima.forms import *

app_name="clima"

def base2(request):
    profileinst = profile.objects.filter(user=request.user)                     
    context={
        'profileinst':profileinst,
    }
    return render(request,'clima/clima_base.html',context)


def clima_index(request):
    profileinst = profile.objects.filter(user=request.user)                     
    context={
        'profileinst':profileinst,
    }
    return render(request,'clima/UserDashboard_clima.html',context)



def mylogin_clima(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Logged In Successfully!!')
            return redirect('clima:clima_indexurls')
        else:
            messages.error(request,'Something Went Wrong')
            return redirect('clima:Clima_Loginurls')
    return render(request,'clima/login_clima.html')


@login_required
def clima_userprofile(request):
    profileinst = profile.objects.filter(user=request.user)                     
    context={
        'profileinst':profileinst,
    }
    return render(request,'clima/profile_clima.html',context)

@login_required
def mylogout_clima(request):
    logout(request)
    messages.success(request,'Logged Out Successfully!!')
    return redirect('clima:Clima_Loginurls')



@login_required
def Profile_setting_clima(request):
    profileinst = profile.objects.filter(user=request.user)                     
    context={
        'profileinst':profileinst,
    }
    return render(request,'clima/profile_setting_clima.html',context)


@login_required
def kyc_clima(request):
    if request.method == 'POST':
        form = climaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            send_mail(
                'CLIMA KYC',
                'New KYC Submitted',
                'opinverse0@gmail.com',
                ['opinverse0@gmail.com','shaan.anand1995@gmail.com'] ,
                fail_silently=False,
            )
    else:
        form = climaForm()
    context={
        'form':form,
    }
    return render(request,'clima/kyc_clima.html',context)


@login_required
def clima_activites(request):
    return render(request,'clima/activities_clima.html')


@login_required
def qualification_clima(request):
    return render(request,'clima/qualifications_clima.html')


@login_required
def documents_clima(request):
    return render(request,'clima/documents_clima.html')


@login_required
def billingpayments_clima(request):
    return render(request,'clima/billing&payments_clima.html')


@login_required
def clima_wallet_dashboard(request):
    return render(request,'clima/clima_wallet_dashboard.html')


@login_required
def clima_wallet_history(request):
    return render(request,'clima/clima_wallet_history.html')

@login_required
def clima_User_Subscription(request):
    return render(request,'clima/clima_Subscription.html')

@login_required
def calender_clima(request):
    return render(request,'clima/clima_calender.html')



@login_required
def clima_CRM_Contacts(request):
    return render(request,'clima/clima_crm_contacts.html')


@login_required
def clima_CRM_companies(request):
    return render(request,'clima/clima_crm_companies.html')


@login_required
def clima_CRM_deals(request):
    return render(request,'clima/clima_crm_deals.html')


@login_required
def clima_CRM_leads(request):
    return render(request,'clima/clima_crm_leads.html')

@login_required
def clima_task(request):
    return render(request,'clima/clima_task.html')

@login_required
def clima_brands(request):
    return render(request,'clima/clima_brands.html')



@login_required
def clima_projects(request):
    return render(request,'clima/clima_projects.html')


@login_required
def clima_supportticket_create(request):
    return render(request,'clima/clima_supportticket_create.html')


@login_required
def clima_supportticket_details(request):
    return render(request,'clima/clima_supportticket_details.html')

@login_required
def clima_supportticket_history(request):
    return render(request,'clima/clima_supportticket_history.html')

@login_required
def gig_all(request):
    return render(request,'clima/gig_viewall.html')



@login_required
def gig_new(request):
    return render(request,'clima/gig_new.html')



@login_required
def gig_previous(request):
    return render(request,'clima/gig_previous.html')


@login_required
def gig_feedback(request):
    return render(request,'clima/gig_feedback.html')












