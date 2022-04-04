from django.contrib import admin
from .models import Product
from .models import Profile
from .models import Review
# Register your models here.

@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'brand', 'average_cost', 'product_category', 'release_date', 'description'] 

@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'date_of_birth', 'address', 'city', 'country', 'user_photo']

@admin.register(Review)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product_rating', 'review', 'date']