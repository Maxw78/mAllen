from sqlite3 import Date
from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100, blank=False)
    brand = models.CharField(max_length=100, blank=False)
    average_cost = models.IntegerField(default=0, blank=False)
    CATEGORY_CHOICES = [('TV', 'TV'), ('Tablet', 'Tablet'), ('Phone', 'Phone')]
    category = models.CharField(max_length=15, category=CATEGORY_CHOICES, blank=False)
    release_date = models.DateField(default=Date, blank=False)
    description = models.CharField(max_length=100, blank=False)

def _str_ (self):
    return self.Product

class Profile(models.model):
    profile_id = models.AutoField(primary_key=True, blank=False)
    full_name = models.CharField(max_length=30, blank=False)
    date_of_birth = models.DateField(default=Date, blank=False)
    address = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)
    COUNTRY_CHOICES = [('UK', 'UK'), ('France', 'France'), ('Germany', 'Germany'), ('Spain', 'Spain')]
    country = models.CharField(max_length=15, category=COUNTRY_CHOICES, blank=False)
    user_photo = models.ImageField(upload_to = 'user_photo/')

def _str_ (self):
    return self.Profile

class Review(models.model):
    review_id = models.AutoField(primary_key=True, blank=False)
    product_rating = models.IntegerField(default=0, blank=False)
    review = models.CharField(max_length=30, blank=False)
    date = models.DateField(default=Date, blank=False)

def _str_ (self):
    return self.Review
    