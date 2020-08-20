from django.db import models
from datetime import date

# Create your models here.

class category(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Product(models.Model):

    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    distributer = models.CharField(max_length=20, blank=True)
    category = models.ForeignKey('category', on_delete=models.CASCADE,default=None)
    size = models.CharField(max_length=10, blank= True)
    weight = models.IntegerField(default = 0)
    quantity = models.IntegerField(default=1)
    cost_price = models.CharField(max_length=50)
    selling_price = models.CharField(max_length=50)
    mfg_date = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    exp_date = models.DateField(auto_now=False, auto_now_add=False)
    #image

    def __str__(self):
        return self.name
    

class Order(models.Model):
    models.DateTimeField(auto_now=True, auto_now_add=True)
    product = models.ManyToManyField("inventory.Product")
    total_cost = models.CharField( max_length=50)
    # customer
    # paid/pending

    

class DailyDeliveries():
    pass