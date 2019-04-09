from __future__ import unicode_literals

from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render

from adminp.models import Add_staff,Add_products
# Create your views here.
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
	return render(request,'staff/addsales.html',{'data':a})

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
	productId=request.GET.get('productId', None)
	print(productId)
	j=Add_products.objects.filter(id=productId).values()
	print(j)
	print("--------------------------------------")
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
	if request.method=="POST":
		uid=request.session['id']
		print(id)
		name=request.POST.get('name','')
		uname=request.POST.get('uname','')
		phno=request.POST.get('phno','')
		
		Add_staff.objects.filter(id=uid).update(name=name,uname=uname,number=phno)
		
		return render(request,'staff/dashboard.html',{'suc':'Updated Successfully'})
	else:
		uid=request.session['id']
		print(uid)
		a=Add_staff.objects.all().filter(id=uid).values()
		print(a)
		
		return render(request,'staff/account_setting.html',{'data': a})
def logout(request):
	return HttpResponseRedirect('/staff/login')





	