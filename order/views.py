from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from authentication.models import CustomUserModel
from core.models import ProductVarient,Product
from .models import OrderItem,Order
# Create your views here.
class AddToCartView(View):
    @method_decorator(login_required)
    def get(self,request,*args,**kwargs):
        username=request.user
        user=CustomUserModel.objects.get(username=username)
        product_slug=kwargs['slug']
        productvarient=ProductVarient.objects.get(slug=product_slug)
        product=Product.objects.get(product_id=productvarient.product_id.product_id)
        orderitem=OrderItem.objects.create(product_id=product,price=productvarient.sale_price,quantity=1)
        total=orderitem.quantity*orderitem.price
        Order.objects.create(order_item=orderitem,total=total,status="not placed",user_id=user)
        return render(request,'cart.html',{})

