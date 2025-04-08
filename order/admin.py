from django.contrib import admin
from .models import Order,OrderItem
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['order_id','user_id','total','status','created_at']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display=['order_item_id','order_id','product_id','quantity','price']