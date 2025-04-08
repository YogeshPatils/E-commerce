from django.urls import path
from .views import AddToCartView,CartView

urlpatterns=[
    path('addtocart/<slug:slug>/',AddToCartView.as_view(),name='addtocart'),
    path('cart/<int:user_id>/',CartView.as_view(),name='cart'),
]