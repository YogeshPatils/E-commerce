from django.shortcuts import render,redirect
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
    def get(self, request, *args, **kwargs):
        from django.utils import timezone
        user = request.user
        product_slug = kwargs['slug']
        productvarient = ProductVarient.objects.get(slug=product_slug)
        product = productvarient.product

        # Get or create an existing "not placed" order (cart)
        order, created = Order.objects.get_or_create(user_id=user, status="not placed", defaults={
            'total': 0,
            'created_at': timezone.now()
        })

        # Add item to order
        # Check if the product is already in the cart
        order_item, created = OrderItem.objects.get_or_create(
            order_id=order,
            product_id=product,
            defaults={'quantity': 1, 'price': productvarient.sale_price}
        )

        # If it already exists, increase the quantity
        if not created:
            order_item.quantity += 1
            order_item.save()


        # Update order total
        all_items = OrderItem.objects.filter(order_id=order)
        total = sum(item.price * item.quantity for item in all_items)
        order.total = total
        order.save()

        return redirect('cart', user_id=user.id)

class CartView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        order = Order.objects.filter(user_id=user_id, status="not placed").order_by('-created_at').first()

        # Get all order items linked to those orders

        order_items = OrderItem.objects.filter(order_id=order).select_related('product_id', 'order_id')
        for item in order_items:
            item.subtotal = item.price * item.quantity

        context = {
            'order_items':order_items,
            'order':order
        }
        return render(request, 'order/cart.html', context)


