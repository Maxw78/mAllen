from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='WebShop'),
    path('about/', views.AboutUs, name='WebShop-About'),
    path('contactus/', views.ContactUs, name='WebShop-Contact'),
    path('products/', views.Products, name='WebShop-Products'),
]