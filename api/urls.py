from django.urls import path
from .views import userView,productView
urlpatterns=[
    path('userapi/',userView,name='userapi'),
    path('productapi/',productView,name='productapi'),
]
