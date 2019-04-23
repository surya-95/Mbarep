from __future__ import unicode_literals

from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render

from adminp.models import Add_staff,Add_products
from .models import SaleData,OrderPrdct,ProDet
import datetime
# Create your views here.
def home(request):
	return render(request,'staff/base.html')
def staff_login(request):
	if request.method == "POST":
		uname=request.POST.get('uname','')
		passwrd=request.POST.get('password','')
		print( uname)
		print (passwrd)
		
		r=Add_staff.objects.all().filter(uname=uname,password=passwrd)
		print (r)
		if r.exists():
			for x in r:
				request.session['id']=x.id
			return render(request,'staff/dashboard.html',{'data':r})
		else:
			return render(request,'staff/login.html',{'err':'Invalid username or password'})
	return render(request,'staff/login.html')
def Addsales(request):

	a=Add_products.objects.all()
	return render(request,'staff/addsales1.html',{'data':a})

def fetchProductData(request):
	a=Add_products.objects.all().values()
	print(a)
	print("____________________________________")
	# for x in a:
	# 	value=x.pid
	# 	value2=x.pname
	return JsonResponse({'results': list(a)})
def fetchSelectedProduct(request):
	print("--------------------------------------")
	productId=request.GET.get('productId',None)
	print(productId)
	j=Add_products.objects.filter(id=productId).values()
	print(j)
	print("---------------- ---------------------")
	# for x in a:
	# 	value=x.pid
	# 	value2=x.pname
	return JsonResponse({'rslt': list(j)})


def Updatepaswd(request):
	if request.method=="POST":
		uid=request.session['id']
		up1=request.POST.get('password1','')
		
		up2=request.POST.get('password2','')

		if up1==up2:
			
			f=Add_staff.objects.filter(id=uid).update(password=up1)
			return render(request,"admin/login.html",{'suc':'Successfully Changed Password!!! Please Login again to continue'})
		else:
			
			return render(request,"admin/update_password.html",{'err':"Two password didn't match"})
	else:
		return render(request,"admin/update_password.html")	

def editprofile(request):
	print("_____________________________________")
	if request.method=="POST":
		uid=request.session['id']
		print(id)
		name=request.POST.get('name','')
		print(name)
		uname=request.POST.get('uname','')
		print(uname)
		phno=request.POST.get('phno','')
		print(phno)
		address=request.POST.get('address','')
		print(address)
		gender=request.POST.get('gender','')
		print(gender)
		email=request.POST.get('email','')
		print(email)
		Add_staff.objects.filter(id=uid).update(name=name,uname=uname,number=phno,email=email,address=address,gender=gender)
		
		return render(request,'staff/dashboard.html',{'suc':'Updated Successfully'})
	else:
		uid=request.session['id']
		print(uid)
		a=Add_staff.objects.all().filter(id=uid).values()
		print(a)
		
		return render(request,'staff/account_setting.html',{'data': a})
def logout(request):
	return HttpResponseRedirect('/staff/login')

def savedata(request):
	# rateval=request.POST.getlist('rateValue','')
	# print("+++++++++++++++++=")
	# print(rateval)
	# orderdate=request.POST.get('orderDate','')
	orderdate=request.POST.get('orderDate','')
	print("()()()()()()()()()()()()()()())")
	print(orderdate)
	clientname=request.POST.get('clientName','')
	print(clientname)
	phone=request.POST.get('clientContact','')
	product_id=request.POST.get('hd','')
	print(product_id)
	paid=request.POST.get('paid','')
	
	
	due=request.POST.get('dueValue','')
	total=request.POST.get('totalAmountValue','')
	discout=request.POST.get('discount','')
	grand=request.POST.get('grandTotalValue','')
	# quantity=request.POST.get('grandTotalValue','')
	ob=SaleData(orderdate=orderdate, clientname=clientname, phone=phone, paid=paid, due=due, total=total, discout=discout, grand=grand)
	ob.save()
	# Add_products.objects.filter(id=product_id).update(quantity=quan)
	dt=SaleData.objects.latest('id');
	print("id+++++++++++++++++++++")
	orid=dt.id
	prid=product_id.split(",")
	print(prid)
	
	currentDT = datetime.datetime.now()
	date=currentDT.strftime("%Y/%m/%d")
	time=currentDT.strftime("%H:%M:%S")
	for x in prid:
		dt=Add_products.objects.all().filter(id=x)
		s=OrderPrdct(orderid=orid,product=dt[0].pname,date=date,time=time)
		s.save()    
		# b=ProDet(orderid=orid,product=dt[0].pname,quantity=dt[0].quantity,date=date)
		# b.save()
		# print (quan)
		
		# Add_products.objects.filter(id=x).update(quantity=t)

	# productname = ",".join(productname)
	# print(productname)
	# ob=SaleData(orderdate=orderdate, clientname=clientname, phone=phone, product=productname, subamt=subamt, paid=paid, gst=gst, due=due, total=total, discout=discout, grand=grand)
	# ob.save()
	a=Add_products.objects.all()
	return render(request,'staff/addsales1.html',{'data':a})
def editprofile(request):
	id=request.session['id']
	a=Add_staff.objects.all().filter(id=id)
	return render(request,'staff/account_setting.html',{'data':a})




	