from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)

class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_type=models.CharField(max_length=100)
    created_at=models.DateField()
    # Product_image=models.ImageField(upload_to='product_images/')

class ProductCategory(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)

class ProductVarient(models.Model):
    varient_id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    attribute=models.CharField(max_length=100)
    value=models.IntegerField()
    extra_price=models.DecimalField(max_digits=10,decimal_places=2)
    image1=models.ImageField(upload_to='product_images/')
    image2=models.ImageField(upload_to='product_images/')
    image3=models.ImageField(upload_to='product_images/')

class ProductAttribute(models.Model):
    attribute_id=models.IntegerField(primary_key=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    attribute=models.CharField(max_length=100)
    value=models.IntegerField()

# class Order(models.Model):
#     order_id=models.AutoField(primary_key=True)
#     user_id=models.ForeignKey(User,on_delete=models.CASCADE)
#     total=models.DecimalField(max_digits=10,decimal_places=2)
#     status=models.CharField(max_length=20)
#     created_at=models.DateTimeField()

# class OrderItem(models.Model):
#     order_item_id=models.AutoField(primary_key=True)
#     order_id=models.ForeignKey(Order,on_delete=models.CASCADE)
#     product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
#     quantity=models.IntegerField()
#     price=models.DecimalField(max_digits=10,decimal_places=2)

# class Cart(models.Model):
#     cart_id=models.AutoField(primary_key=True)
#     user_id=models.ForeignKey(User,on_delete=models.CASCADE)
#     product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
#     quantity=models.IntegerField()

# class Payment(models.Model):
#     payment_id=models.AutoField(primary_key=True)
#     order_id=models.ForeignKey(Order,on_delete=models.CASCADE)
#     user_id=models.ForeignKey(User,on_delete=models.CASCADE)
#     amount=models.DecimalField(max_digits=10,decimal_places=2)
#     status=models.CharField(max_length=20)
#     created_at=models.DateTimeField()

class Review(models.Model):
    review_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    rating=models.DecimalField(max_digits=4,decimal_places=2)
    review_text=models.TextField()
    created_at=models.DateTimeField()

class DigitalProduct(models.Model):
    digital_id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    file_url=models.TextField()












    