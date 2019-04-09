# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
    price=models.IntegerField(default='')
class Add_staff(models.Model):
    name=models.CharField(max_length=30,default='')
    uname=models.CharField(max_length=30,default='')
    number=models.CharField(max_length=10,default='')
    password=models.CharField(max_length=30,default='')
