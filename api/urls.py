from django.urls import path
from .views import userView,productView,productVarientView
urlpatterns=[
    path('userapi/',userView,name='userapi'),
    path('productvarientapi/',productVarientView,name='productvarientapi'),
    path('productapi/',productView,name='productapi'),
]
