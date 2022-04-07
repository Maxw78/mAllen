from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.home, name='WebShop'),
    path('about/', views.AboutUs, name='WebShop-About'),
    path('contactus/', views.ContactUs, name='WebShop-Contact'),
    path('products/', views.Products, name='WebShop-Products'),
    path('<int:product_id>/', views.Product_page, name='WebShop-Product_page'),
    path('review/', views.Review, name='review'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
]