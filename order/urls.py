from django.urls import path
from .views import AddToCartView

urlpatterns=[
    path('addtocart/<slug:slug/>',AddToCartView.as_view(),name='addtocart')
]