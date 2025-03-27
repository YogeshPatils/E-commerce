from django.urls import path
from .views import passwordValidate,ResetPasswordView,SignUpView,SignInView,emailValidateView,phoneValidateView,SignOutView,userNameValidateView,IdentifyUserView,ValidateOtpView

urlpatterns=[
    path('signup/',SignUpView.as_view(),name='signup'),
    path('signin/',SignInView.as_view(),name='signin'),
    path('signout/',SignOutView.as_view(),name='signout'),
    path('identifyuser/',IdentifyUserView.as_view(),name='identify'),
    path('otpvalidate/<str:username>',ValidateOtpView.as_view(),name='otpcheck'),
    path('resetpassword/<str:username>',ResetPasswordView.as_view(),name='resetpwd'),
    path('usernamevalidate/',userNameValidateView,name='usernamevalidate'),
    path('phonevalidate/',phoneValidateView,name='phonevalidate'),
    path('emailvalidate/',emailValidateView,name='emailvalidate'),
    path('pwdvalidate/',passwordValidate,name='pwdvalidate'),
]
