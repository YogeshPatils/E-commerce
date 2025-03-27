from django.contrib import admin
from .models import Product,Category,Review,ProductAttribute,ProductCategory,ProductVarient,DigitalProduct
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['category_id','name','category_image','parent_category']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['product_id','name','brand','description','category_id','product_type','created_at']


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display=['product_id','category_id']

@admin.register(ProductVarient)
class ProductVarientadmin(admin.ModelAdmin):
    list_display=['varient_id','product','attribute','value','extra_price','image1','image2','image3','original_price','sale_price','discount_per','stock','color']

@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display=['attribute_id','product_id','attribute','value']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display=['review_id','user_id','product_id','rating','review_text','created_at']

@admin.register(DigitalProduct)
class DigitalProductAdmin(admin.ModelAdmin):
    list_display=['digital_id','product_id','file_url']
