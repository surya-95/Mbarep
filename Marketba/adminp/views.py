from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Admin_login,Add_products,Add_staff,Add_category
# Create your views here.
def admin_login(request):
	if request.method == "POST":
		uname=request.POST.get('uname','')
		passwrd=request.POST.get('password','')
		print( uname)
		print (passwrd)
		
		r=Admin_login.objects.all().filter(username=uname,password=passwrd)
		print (r)
		if r.exists():
			return render(request,'admin/dashboard.html')
		else:
			return render(request,'admin/login.html',{'er_msg':'Invalid username or password'})
	return render(request,'admin/login.html')
def Addprod(request):
	if request.method == "POST":
		pname=request.POST.get('pname','')
		category=request.POST.get('category','')
		quantity=request.POST.get('quantity','')
		price=request.POST.get('price','')

		r=Add_products.objects.all().filter(pname=pname)
		print(r)
		if r.exists():
			return render(request,'admin/add_products.html')
		else:
			a=Add_products(pname=pname,category=category,quantity=quantity,price=price)
			a.save()
	return render(request,'admin/add_products.html')
def Addstaff(request):
	if request.method == "POST":
		name=request.POST.get('name','')
		email=request.POST.get('email','')
		phno=request.POST.get('phno','')
		print(phno)
		password=request.POST.get('password','')

		r=Add_staff.objects.all().filter(name=name)
		print(r)
		if r.exists():
			return render(request,'admin/add_staff')
		else:
			a=Add_staff(name=name,Email=email,number=phno,password=password)
			a.save()
	return render(request,'admin/add_staff.html')
def Addcategory(request):
	if request.method == "POST":
		category=request.POST.get('category','')

		r=Add_category.objects.all().filter(category=category)
		print(r)
		if r.exists():
			return render(request,'admin/add_category')
		else:
			a=Add_category(category=category)
			a.save()
	return render(request,'admin/add_category.html')
def logout(request):
	return HttpResponseRedirect('/admin/login')
