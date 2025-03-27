from django.shortcuts import render
from django.views import View
from .models import Category,Product,ProductVarient
# Create your views here.
class HomeView(View):
    def get(self,request,*args,**kwargs):
        qs=Category.objects.filter(parent_category=None)
        
        return render(request,'authentication/home.html',{'categorys':qs}) 
    
class CategoryView(View):
    def get(self,request,*args,**kwargs):
        obj=Category.objects.get(name=kwargs.get('category'))
        product_data=Product.objects.filter(category_id=obj)
        varient_data=ProductVarient.objects.filter(product__in=product_data)
        data=zip(product_data,varient_data)
        return render(request,'core/category.html',{'data':data})

class ProductView(View):
    def get(self,request,*args,**kwargs):
        vd=ProductVarient.objects.get(varient_id=kwargs.get('varient_id'))
        pd=Product.objects.get(name=vd.product)
        return render(request,'core/productdetail.html',{'vd':vd,'pd':pd})