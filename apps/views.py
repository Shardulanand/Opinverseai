from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from apps.models import *
from django.contrib.auth.decorators import login_required
from apps.forms import *
from django.core.mail import send_mail


app_name="apps"

def errorHandle404(request):
    return render(request,'apps/404.html')




def mylogin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Logged In Successfully!!')
            return redirect('apps:Myindex')
        else:
            messages.error(request,'Something Went Wrong')
            return redirect('apps:myloginurls')
    return render(request,'apps/login.html')

@login_required
def index(request):
    return render(request,'apps/UserDashboard.html')

def base(request):
    profileinst = profile.objects.filter(user=request.user)                     
    context={
        'profileinst':profileinst,
    }
    return render(request,'apps/base.html',context)


def mylogout(request):
    logout(request)
    messages.success(request,'Logged Out Successfully!!')
    return redirect('apps:myloginurls')



@login_required
def userprofile(request):
    profileinst = profile.objects.filter(user=request.user)                     
    context={
        'profileinst':profileinst,
    }
    return render(request,'apps/profile.html',context)

@login_required
def User_Subscription(request):
    return render(request,'apps/Subscription.html')

@login_required
def Profile_setting(request):
    profileinst = profile.objects.filter(user=request.user)                     
    context={
        'profileinst':profileinst,
    }
    return render(request,'apps/profile_setting.html',context)


# @login_required
# def User_Kyc(request):
#     profileinst = profile.objects.all()
#     profileinst1= profile.objects.filter(user=request.user)     
#     if request.method =="POST":
#         form=user_kyc_dima_Form(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#         else:
#             print(form.errors)
#             return redirect('apps:profileurls')
#     form=user_kyc_dima_Form()         
#     context={
#         'profileinst':profileinst,
#         'profileinst1':profileinst1,
#         'form':form,
#     }
#     return render(request,'apps/User_kyc.html',context)



@login_required
def User_Kyc(request):
    if request.method == 'POST':
        form = DimaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            send_mail(
                'DIMA KYC',
                'New KYC Submitted',
                'opinverse0@gmail.com',
                ['opinverse0@gmail.com','shaan.anand1995@gmail.com'] ,
                fail_silently=False,
            )
    else:
        form = DimaForm()
    context={
        'form':form,
    }
    return render(request, 'apps/User_kyc.html', context)


@login_required
def Success_login(request):
    return render(request,'apps/success_login.html')


@login_required
def calender_dima(request):
    return render(request,'apps/calender.html')


@login_required
def activites(request):
    return render(request,'apps/activities.html')


@login_required
def qualifications(request):
    return render(request,'apps/qualifications.html')

@login_required
def documents(request):
    return render(request,'apps/documents.html')

@login_required
def billingpayment(request):
    return render(request,'apps/billing&Payment.html')

@login_required
def wallet_dashboard(request):
    return render(request,'apps/wallet_dashboard.html')


@login_required
def wallet_history(request):
    return render(request,'apps/wallet_history.html')

@login_required
def client_all(request):
    return render(request,'apps/client_viewall.html')



@login_required
def client_new(request):
    return render(request,'apps/client_new.html')



@login_required
def client_previous(request):
    return render(request,'apps/client_previous.html')


@login_required
def client_feedback(request):
    return render(request,'apps/client_feedback.html')


@login_required
def CRM_Contacts(request):
    return render(request,'apps/crm_contacts.html')


@login_required
def CRM_companies(request):
    return render(request,'apps/crm_companies.html')


@login_required
def CRM_deals(request):
    return render(request,'apps/crm_deals.html')


@login_required
def CRM_leads(request):
    return render(request,'apps/crm_leads.html')




@login_required
def task(request):
    return render(request,'apps/task.html')


@login_required
def brands(request):
    return render(request,'apps/brands.html')

@login_required
def projects(request):
    return render(request,'apps/projects.html')


@login_required
def team(request):
    return render(request,'apps/teams.html')


@login_required
def supportticket_create(request):
    return render(request,'apps/supportticket_create.html')



@login_required
def supportticket_details(request):
    return render(request,'apps/supportticket_details.html')


@login_required
def supportticket_history(request):
    return render(request,'apps/supportticket_history.html')



@login_required
def tutorials_courses(request):
    return render(request,'apps/tutorials_courses.html')
