from django.contrib import admin
from .models import CustomUserModel
# Register your models here.
@admin.register(CustomUserModel)
class CustomUserAdmin(admin.ModelAdmin):
    list_display=['gender','phone','date_of_birth']