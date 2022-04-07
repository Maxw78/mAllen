from sqlite3 import Date
from unicodedata import name
from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30, null=False)
    date_of_birth = models.DateField(null=True)
    address = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)
    COUNTRY_CHOICES = [('UK', 'UK'), ('France', 'France'), ('Germany', 'Germany'), ('Spain', 'Spain')]
    country = models.CharField(max_length=15, choices=COUNTRY_CHOICES, null=False)
    user_photo = models.ImageField(default='default.jpg', upload_to = 'user_photo/')

def __str__(self):
    return f'Profile for {self.user.username}'

class Review(models.Model):
    review_id = models.AutoField(primary_key=True, blank=False)
    product_rating = models.IntegerField(default=0, validators=[MaxValueValidator(5)], blank=False)
    review = models.TextField(max_length=255, blank=False)
    date = models.DateField()
    profile = models.ForeignKey(Profile, db_column='full_name', null=True, blank=True, on_delete=models.CASCADE)

def __str__(self):
    return self.product_rating


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=40, blank=False)
    brand = models.CharField(max_length=30, blank=False)
    average_cost = models.IntegerField(default=0, blank=False)
    CATEGORY_CHOICES = [('TV', 'TV'), ('Laptop', 'Laptop'), ('Phone', 'Phone')]
    product_category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    release_date = models.DateField()
    description = models.TextField(max_length=100, blank=False)
    product_photo = models.ImageField(default='default.jpg', upload_to = 'product_photo/')
    review = models.ManyToManyField(Review, blank=True)

def __str__(self):
    return self.product_name