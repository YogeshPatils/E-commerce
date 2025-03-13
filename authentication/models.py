from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CustomUserModel(User):
    gender=models.CharField(max_length=10,choices=[['male','Male'],['female','Female'],['others','Others']])
    date_of_birth=models.DateField()
    phone=models.IntegerField()
    otp=models.IntegerField(null=True,blank=True)
    otp_expiry=models.DateTimeField(null=True,blank=True)
    


