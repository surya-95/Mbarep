from django.db import models

# Create your models here.
class SaleData(models.Model):
    orderdate=models.CharField(max_length=60,default='')
    clientname=models.CharField(max_length=60,default='')
    phone=models.CharField(max_length=60,default='')
    # product=models.CharField(max_length=60,default='')
    
    paid=models.CharField(max_length=60,default='')
    
    due=models.CharField(max_length=60,default='')
    total=models.CharField(max_length=60,default='')
    discout=models.CharField(max_length=60,default='')
    grand=models.CharField(max_length=60,default='')
    
class OrderPrdct(models.Model):
    orderid=models.CharField(max_length=60,default='')
    product=models.CharField(max_length=60,default='')
    date=models.CharField(max_length=60,default='')
    time=models.CharField(max_length=60,default='')
class ProDet(models.Model):
    orderid=models.CharField(max_length=60,default='')
    product=models.CharField(max_length=60,default='')
    date=models.CharField(max_length=60,default='')
    quantity=models.CharField(max_length=60,default='')
