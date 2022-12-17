from django.db import models
from django.contrib import admin
class Book(models.Model):
    bookid = models.CharField(max_length=8,primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    email = models.EmailField()
    author = models.CharField(max_length=100)

class BookAdmin(admin.ModelAdmin):
    list_display = ('bookid','name','price','email','author')

# Create your models here.
