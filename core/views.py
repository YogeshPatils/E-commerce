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

class SearchView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        data = []

        if query:
            products = Product.objects.filter(name__icontains=query)
            varient_map = {v.product.product_id: v for v in ProductVarient.objects.filter(product__in=products)}
            data = [(pd, varient_map.get(pd.product_id)) for pd in products]

        return render(request, 'core/search_results.html', {'data': data, 'query': query})