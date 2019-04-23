from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Admin_login,Add_category,Add_products,Add_staff
from staff.models import SaleData,OrderPrdct
# Create your views here.
def home(request):
	return render(request,'admin/index.html')
def graph(request):
	return render(request,'admin/graph.html')
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
			return render(request,'admin/login.html',{'err':'Invalid username or password'})
	return render(request,'admin/login.html')
def Addprod(request):
	c=Add_category.objects.all()
	if request.method == "POST":
		pname=request.POST.get('pname','')
		category=request.POST.get('category','')
		quantity=request.POST.get('quantity','')
		price=request.POST.get('price','')
		desc=request.POST.get('desc','')
		mfd=request.POST.get('mfd','')
		exd=request.POST.get('exd','')
		gst=request.POST.get("gst",'')
		gstp=(float(price) * float(gst))/100
		tprice=float(price)+float(gstp)
		
		r=Add_products.objects.all().filter(pname=pname,mfd=mfd,exd=exd,category=category)
		print(r)
		if r.exists():
			return render(request,'admin/add_products.html',{'data':c ,'err':'Already Exist'})
		else:
			
			a=Add_products(pname=pname,category=category,quantity=quantity,price=tprice,amount=price,mfd=mfd,exd=exd,desc=desc,gst=gst)
			a.save()
	return render(request,'admin/add_products.html',{'data':c,'suc':'Successfully Added'})
def Addstaff(request):
	if request.method == "POST":
		name=request.POST.get('name','')
		uname=request.POST.get('uname','')
		phno=request.POST.get('phno','')
		password=request.POST.get('password','')
		address=request.POST.get('address','')
		email=request.POST.get('email','')
		gender=request.POST.get('gender','')
		print(gender)
		r=Add_staff.objects.all().filter(name=name,number=phno)
		print(r)
		if r.exists():
			return render(request,'admin/add_staff.html',{'err':'Already Exist'})
		else:
			a=Add_staff(name=name,uname=uname,number=phno,address=address,email=email,gender=gender,password=password)
			a.save()
	return render(request,'admin/add_staff.html',{'suc':'Successfully Added'})
def Addcategory(request):
	if request.method == "POST":
		category=request.POST.get('category','')

		r=Add_category.objects.all().filter(category=category)
		print(r)
		if r.exists():
			return render(request,'admin/add_category',{'err':'Already Exist'})
		else:
			a=Add_category(category=category)
			a.save()
	return render(request,'admin/add_category.html',{'suc':'Successfully Added'})
def viewcategory(request):
	a=Add_category.objects.all()
	return render(request,'admin/view_category.html',{'data': a})




		
def viewstaff(request):
	a=Add_staff.objects.all()
	return render(request,'admin/view_staff.html',{'data': a})
	


		
def viewprod(request):
	a=Add_products.objects.all()
	return render(request,'admin/view_products.html',{'data': a})
	

		
def editcategory(request):
	if request.method=="POST":
		id=request.POST.get('id','')
		catg=request.POST.get('category','')
		Add_category.objects.filter(id=id).update(category=catg)
		a=Add_category.objects.all()
		return render(request,'admin/view_category.html',{'data': a,'suc':'Updated Successfully'})
	else:
		cid=request.GET.get('id','')
		a=Add_category.objects.all().filter(id=cid)
		return render(request,'admin/edit_category.html',{'data': a})
def editprod(request):
	if request.method=="POST":
		id=request.POST.get('id','')
		print(id)
		pname=request.POST.get('pname','')
		catg=request.POST.get('category','')
		quantity=request.POST.get('quantity','')
		price=request.POST.get('price','')
		desc=request.POST.get('desc','')
		mfd=request.POST.get('mfd','')
		exd=request.POST.get('exd','')
		gst=request.POST.get('gst','')
		gstp=(float(price) * float(gst))/100
		tprice=float(price)+float(gstp)
		
		Add_products.objects.filter(id=id).update(pname=pname,category=catg,quantity=quantity,price=tprice,amount=price,desc=desc,exd=exd,mfd=mfd,gst=gst)
		a=Add_products.objects.all()
		return render(request,'admin/view_products.html',{'data': a,'suc':'Updated Successfully'})
	else:
		cid=request.GET.get('id','')
		print(cid)
		a=Add_products.objects.all().filter(id=cid).values()
		print(a)
		b=Add_category.objects.all()
		return render(request,'admin/edit_products.html',{'data': a , 'cat':b})
def Updatepaswd(request):
	if request.method=="POST":
		uid=request.session['id']
		up1=request.POST.get('password1','')
		
		up2=request.POST.get('password2','')

		if up1==up2:
			
			f=Admin_login.objects.filter(id=uid).update(password=up1)
			return render(request,"admin/login.html",{'suc':'Successfully Changed Password!!! Please Login again to continue'})
		else:
			
			return render(request,"admin/update_password.html",{'err':"Two password didn't match"})
	else:
		return render(request,"admin/update_password.html")
def viewtrans(request):
	a=SaleData.objects.all()
	b=OrderPrdct.objects.all()
	return render(request,"admin/viewtrans.html",{'data':a,'dat':b})

def logout(request):
	return HttpResponseRedirect('/admin/login')
