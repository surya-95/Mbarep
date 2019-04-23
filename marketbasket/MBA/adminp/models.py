# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.
class Admin_login(models.Model):
    username=models.CharField(max_length=30,default='')
    password=models.CharField(max_length=30,default='')
class Add_category(models.Model):
    category=models.CharField(max_length=30,default='')
class Add_products(models.Model):
    pname=models.CharField(max_length=30,default='')
    category=models.CharField(max_length=30,default='')
    quantity=models.CharField(max_length=30,default='')
    amount=models.FloatField(default='')
    price=models.FloatField(default='')
    date = models.DateField(default=datetime.now())
    desc=models.CharField(max_length=30,default='')
    mfd=models.CharField(max_length=30,default='')
    exd=models.CharField(max_length=30,default='')
    gst=models.FloatField(default='')
class Add_staff(models.Model):
    name=models.CharField(max_length=30,default='')
    uname=models.CharField(max_length=30,default='')
    number=models.CharField(max_length=10,default='')
    password=models.CharField(max_length=30,default='')
    address=models.CharField(max_length=100,default='')
    email=models.CharField(max_length=30,default='')
    gender=models.CharField(max_length=6,default='')