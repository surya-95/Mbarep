from django.conf.urls import url
from staff import views 

urlpatterns = [
    # url(r'^start/',ld),
    url(r'^login/',views.staff_login),
    url(r'^addsales/',views.Addsales),
    url(r'^fetchProductData/',views.fetchProductData),
    url(r'^fetchSelectedProduct/',views.fetchSelectedProduct),
    url(r'^updatepaswd/',views.Updatepaswd),
    url(r'^logout/',views.logout),
    
    
]