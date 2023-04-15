
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from clima.models import *
from django.contrib.auth.decorators import login_required
from apps.forms import *
from frama.forms import *
from django.core.mail import send_mail

app_name="clima"

def mylogin_frama(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Logged In Successfully!!')
            return redirect('frama:frama_indexurls')
        else:
            messages.error(request,'Something Went Wrong')
            return redirect('frama:mylogin_framaurls')
    return render(request,'frama/frama_login.html')



def frama_index(request):
    return render(request,'frama/framaUserDashboard.html')

def frama_Profile(request):
    profileinst = profile.objects.filter(user=request.user)                     
    context={
        'profileinst':profileinst,
    }
    return render(request,'frama/frama_profile.html',context)




@login_required
def mylogout_frama(request):
    logout(request)
    messages.success(request,'Logged Out Successfully!!')
    return redirect('frama:mylogin_framaurls')

@login_required
def frama_userprofile_setting(request):
    profileinst = profile.objects.filter(user=request.user)                     
    context={
        'profileinst':profileinst,
    }
    return render(request,'frama/frama_profile_setting.html',context)




@login_required
def kyc_frama(request):
    if request.method == 'POST':
        form = framaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            send_mail(
                'FRAMA KYC',
                'New KYC Submitted',
                'opinverse0@gmail.com',
                ['opinverse0@gmail.com','shaan.anand1995@gmail.com'] ,
                fail_silently=False,
            )
    else:
        form = framaForm()
    context={
        'form':form,
    }
    return render(request,'frama/kyc_frama.html',context)


@login_required
def frama_activities(request):
    return render(request,'frama/frama_activities.html')


@login_required
def frama_qualification(request):
    return render(request,'frama/frama_qualifications.html')



@login_required
def frama_documents(request):
    return render(request,'frama/frama_documents.html')

@login_required
def frama_billingpayments(request):
    return render(request,'frama/frama_billing&payments.html')


@login_required
def frama_User_Subscription(request):
    return render(request,'frama/frama_Subscription.html')

@login_required
def calender_frama(request):
    return render(request,'frama/frama_calender.html')

@login_required
def frama_gig_all(request):
    return render(request,'frama/frama_gig_viewall.html')



@login_required
def frama_gig_new(request):
    return render(request,'frama/frama_gig_new.html')



@login_required
def frama_gig_previous(request):
    return render(request,'frama/frama_gig_previous.html')


@login_required
def frama_gig_feedback(request):
    return render(request,'frama/frama_gig_feedback.html')



@login_required
def frama_task(request):
    return render(request,'frama/frama_task.html')

@login_required
def frama_brands(request):
    return render(request,'frama/frama_brands.html')


@login_required
def frama_projects(request):
    return render(request,'frama/frama_projects.html')

@login_required
def frama_CRM_Contacts(request):
    return render(request,'frama/frama_crm_contacts.html')

@login_required
def frama_CRM_companies(request):
    return render(request,'frama/frama_crm_companies.html')

@login_required
def frama_CRM_deals(request):
    return render(request,'frama/frama_crm_deals.html')

@login_required
def frama_CRM_leads(request):
    return render(request,'frama/frama_crm_leads.html')

@login_required
def frama_supportticket_create(request):
    return render(request,'frama/frama_supportticket_create.html')

@login_required
def frama_supportticket_details(request):
    return render(request,'frama/frama_supportticket_details.html')


@login_required
def frama_supportticket_history(request):
    return render(request,'frama/frama_supportticket_history.html')
