from sqlite3 import Date
from unicodedata import name
from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=40, blank=False)
    brand = models.CharField(max_length=30, blank=False)
    average_cost = models.IntegerField(default=0, blank=False)
    CATEGORY_CHOICES = [('TV', 'TV'), ('Tablet', 'Tablet'), ('Phone', 'Phone')]
    product_category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    release_date = models.DateField()
    description = models.TextField(max_length=100, blank=False)

def _str_ (self):
    return self.product_name

class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30, blank=False)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)
    COUNTRY_CHOICES = [('UK', 'UK'), ('France', 'France'), ('Germany', 'Germany'), ('Spain', 'Spain')]
    country = models.CharField(max_length=15, choices=COUNTRY_CHOICES, blank=False)
    user_photo = models.ImageField(default='default.jpg', upload_to = 'user_photo/')

def _str_ (self):
    return f'Profile for {self.user.username}'

class Review(models.Model):
    review_id = models.AutoField(primary_key=True, blank=False)
    product_rating = models.IntegerField(default=0, validators=[MaxValueValidator(5)], blank=False)
    review = models.TextField(max_length=255, blank=False)
    date = models.DateField()

def _str_ (self):
    return self.product_rating
