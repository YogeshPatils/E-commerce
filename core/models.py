from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    category_image=models.ImageField(upload_to='category_image/',blank=True,null=True)
    parent_category=models.ForeignKey("self",null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.TextField()
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_type=models.CharField(max_length=100)
    created_at=models.DateField(auto_now_add=True)
    brand=models.CharField(max_length=100,null=True,blank=True)
    # Product_image=models.ImageField(upload_to='product_images/')
    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)

class ProductVarient(models.Model):
    varient_id=models.AutoField(primary_key=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    attribute=models.CharField(max_length=100,blank=True,null=True)
    value=models.CharField(max_length=500,blank=True,null=True)
    extra_price=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    image1=models.ImageField(upload_to='product_images/',null=True,blank=True)
    image2=models.ImageField(upload_to='product_images/',null=True,blank=True)
    image3=models.ImageField(upload_to='product_images/',null=True,blank=True)
    original_price=models.DecimalField(max_digits=10,decimal_places=2)
    sale_price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    discount_per=models.IntegerField(null=True,blank=True)
    stock=models.IntegerField(null=True,blank=True)
    color=models.CharField(max_length=50,null=True,blank=True)


class ProductAttribute(models.Model):
    attribute_id=models.IntegerField(primary_key=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    attribute=models.CharField(max_length=100)
    value=models.CharField(max_length=500)

class Review(models.Model):
    review_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    rating=models.DecimalField(max_digits=4,decimal_places=2)
    review_text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

class DigitalProduct(models.Model):
    digital_id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    file_url=models.TextField()

class ProductSizeOption(models.Model):
    size_id=models.AutoField(primary_key=True)
    product_varient=models.ForeignKey(ProductVarient,on_delete=models.CASCADE)
    size_category=models.CharField(max_length=100)
    size_name=models.CharField(max_length=100)
    stock_in_qty=models.IntegerField()
