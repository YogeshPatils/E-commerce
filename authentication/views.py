from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUserModel
from .forms import CustomUserForm,IdentifyUserForm,OtpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse
from django.core.mail import send_mail
from django.contrib.auth.models import User
import datetime
import random
from django.utils import timezone
from django.db.models import Q

def get_otp(username):
    obj=CustomUserModel.objects.get(username=username)
    otp=random.randint(1000,9999)
    otp_expiry=timezone.now()+datetime.timedelta(minutes=10)
    obj.otp=otp
    obj.otp_expiry=otp_expiry
    obj.save()
    return otp,otp_expiry



class SignUpView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'authentication/signup.html',{'form':CustomUserForm})
    def post(self,request,*args,**kwargs):
        
        fm=CustomUserForm(data=request.POST)
        if fm.is_valid():
            first_name=fm.cleaned_data.get('first_name')
            last_name=fm.cleaned_data.get('last_name')
            email=fm.cleaned_data.get('email')
            
            fm.save()
            msg=f"Dear {first_name} {last_name}, \n Welcome to Ecommerce, your account has been created successfull \n Thank you"
            send_mail(
                "Account registration",
                msg,
                "yogeshdpatils3@gmail.com",
                [email],
                fail_silently=False
            )
            messages.success(request,'User created successfully')
            return redirect('signin')
        return HttpResponse("INVALID")

class SignInView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'authentication/signin.html',{'form':AuthenticationForm})
    def post(self,request,*args,**kwargs):
        fm=AuthenticationForm(data=request.POST)

        if fm.is_valid():
            username=fm.cleaned_data.get('username')
            password=fm.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,f'Signed in successfully {user.username}')
                return redirect('home')
            return redirect('signin')
        messages.error(request,f'Invalid Credentials')
        return redirect('signin')    
        

class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'authentication/home.html')

class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        messages.success(request,f"Signed out successfully")
        
        return redirect('signin')
        



# @csrf_exempt
# def passwo

class IdentifyUserView(View):
    def get(self,request,*args,**kwargs):
        fm=IdentifyUserForm()
        return render(request,'authentication/identifyuser.html',{'form':fm})
    def post(self,request,*args,**kwargs):
        fm=IdentifyUserForm(request.POST)
        user=None
        if fm.is_valid():
            username_or_email=fm.cleaned_data['username_or_email']
            if CustomUserModel.objects.filter(Q(username=username_or_email)|Q(email=username_or_email)).exists():
                user=CustomUserModel.objects.get(Q(username=username_or_email)|Q(email=username_or_email))
                email=user.email
                otp=get_otp(user.username)
                msg=f'The otp for your password reset is {otp[0]} and it expires at {otp[1]}'
                send_mail(
                    'OTP verification',
                    msg,
                    'yogeshdpatils3@gmail.com',
                    [email],
                    fail_silently=False
                )
            return render(request,'authentication/otpsent.html',{'user':user})
        return render(request,'authentication/otpsent.html',{'user':user})
    
class ValidateOtpView(View):
    def get(self,request,*args,**kwargs):
        fm=OtpForm()
        return render(request,'authentication/otpcheck.html',{'form':fm})
    def post(self,request,*args,**kwargs):
        user=CustomUserModel.objects.get(username=kwargs['username'])
        fm=OtpForm(request.POST)
        if fm.is_valid():
            otp=fm.cleaned_data['otp']
            if user.otp_expiry> timezone.now():
                if user.otp==otp:
                    return redirect('resetpwd',kwargs.get('username'))
                messages.error(request,'Incorrect OTP')
                return redirect('otpcheck',kwargs.get('username'))
            messages.error(request,'time expired')
            return redirect('signin')
        
class ResetPasswordView(View):
    def get(self,request,*args,**kwargs):
        user=User.objects.get(username=kwargs.get('username'))
        fm=SetPasswordForm(user=user)
        return render(request,'authentication/setpwd.html',{'form':fm})
    def post(self,request,*args,**kwargs):
        user=User.objects.get(username=kwargs.get('username'))
        fm=SetPasswordForm(user=user,data=request.POST)
        if fm.is_valid():
            fm.save()
            send_mail(
                'Password Reset',
                'Your password has been reset successfully',
                'yogeshdpatils3@gmail.com',
                [user.email],
                fail_silently=False
            )
            return redirect('signin')
        messages.error(request,'Invalid Credentials')
        return redirect('resetpwd',user.username)
    
# @csrf_exempt
# def signUpValidate(request):
#     import json
#     import re
#     data=json.loads(request.body)
#     username = data.get('username','')
#     phone = data.get('phone','')
#     email = data.get('email','')
#     pwd2 = data.get('repassword','')
#     pwd1 = data.get('password','')

#     if len(username)<=3:
#         return JsonResponse({"user_name_len_error":"username must be atleast 3 charachters"})
#     if User.objects.filter(username=username).exists():
#         return JsonResponse({"user_name_error":"username already has been taken"})
#     if re.search(r'[^a-zA-Z0-9@.+\-_]',username):
#         return JsonResponse({"user_name_char_error":"Letters, digits and @/./+/-/_ only"})
#     # return JsonResponse({"usertrue":True})
#     if not re.match(r'^[6-9][0-9]{9}$',phone):
#         return JsonResponse({"phone_error":"invalid phone number"})
#     # return JsonResponse({"phonetrue":True})
#     if not re.match(r'^[a-zA-Z0-9._]+\@[a-zA-Z0-9-.]+\.[a-zA-Z]{2,}$',email):
#         return JsonResponse({"email_error":"invalid email"})
#     # return JsonResponse({"emailtrue":True})
#     if pwd1!=pwd2:
#         return JsonResponse({"pwd_match_error":"Password do not match"})
#     return JsonResponse({"formtrue":True})



def userNameValidateView(request):
    import json
    import re 
    data=json.loads(request.body)
    username=data['username']
    if len(username)<=3:
        return JsonResponse({"user_name_len_error":"username must be atleast 3 charachters"})
    elif User.objects.filter(username=username).exists():
        return JsonResponse({"user_name_error":"username already has been taken"})
    elif re.search(r'[^a-zA-Z0-9@.+\-_]',username):
        return JsonResponse({"user_name_char_error":"Letters, digits and @/./+/-/_ only"})
    return JsonResponse({"usertrue":True})

    

def phoneValidateView(request):
    import json
    import re
    data=json.loads(request.body)
    phone=data['phone']
    if not re.match(r'^[6-9][0-9]{9}$',phone):
        return JsonResponse({"phone_error":"invalid phone number"})
    return JsonResponse({"phonetrue":True})

def emailValidateView(request):
    import json
    import re
    data=json.loads(request.body)
    email=data['email']
    if not re.match(r'^[a-zA-Z0-9._]+\@[a-zA-Z0-9-.]+\.[a-zA-Z]{2,}$',email):
        return JsonResponse({"email_error":"invalid email"})
    return JsonResponse({"emailtrue":True})

def passwordValidate(request):
    import json
    data=json.loads(request.body)
    pwd=data['password']
    if len(pwd)<8:
        return JsonResponse({"pwd_error":"Your password must contain at least 8 characters and one capital letter and one special number"})
    return JsonResponse({"pwdtrue":True})

def passwordMatchView(request):
    import json
    data=json.loads(request.body)
    pwd2=data['repassword']
    pwd1=data['password']
    if pwd1!=pwd2:
        return JsonResponse({"pwd_match_error":"Password do not match"})
    return JsonResponse({"pwdmatchtrue":True})

    

