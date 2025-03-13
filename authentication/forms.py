from django import forms
from .models import CustomUserModel
from django.contrib.auth.forms import UserCreationForm,SetPasswordForm

class CustomUserForm(UserCreationForm):
    class Meta:
        model=CustomUserModel
        fields=['first_name','last_name','username','phone','email','gender','date_of_birth']
        widgets={
            'date_of_birth':forms.DateInput(attrs={'type':'date'}),
            'email':forms.TextInput(attrs={'required':True})
        }

class IdentifyUserForm(forms.Form):
    username_or_email=forms.CharField(max_length=100)

class OtpForm(forms.Form):
    otp=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter OTP'}))



