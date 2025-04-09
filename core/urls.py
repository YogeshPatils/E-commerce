from django.urls import path
from .views import HomeView,CategoryView,ProductView,SearchView
urlpatterns=[
    path('home/',HomeView.as_view(),name='home'),
    path('category/<str:category>/',CategoryView.as_view(),name='category'),
    path('product/<str:varient_id>/',ProductView.as_view(),name='product'),
    path('search/',SearchView.as_view(),name='search')

]