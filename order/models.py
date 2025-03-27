from django.db import models
from django.contrib.auth.models import User
from core.models import Product

# Create your models here.
class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    total=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=20)
    created_at=models.DateTimeField()

class OrderItem(models.Model):
    order_item_id=models.AutoField(primary_key=True)
    order_id=models.ForeignKey(Order,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)

class Cart(models.Model):
    cart_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()

class Payment(models.Model):
    payment_id=models.AutoField(primary_key=True)
    order_id=models.ForeignKey(Order,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=20)
    created_at=models.DateTimeField()