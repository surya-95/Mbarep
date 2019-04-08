from django.conf.urls import url
from adminp import views 

urlpatterns = [
    # url(r'^start/',ld),
    url(r'^login/',views.admin_login),
    url(r'^addprod/',views.Addprod),
    url(r'^addstaff/',views.Addstaff),
     url(r'^addcategory/',views.Addcategory),
    url(r'^logout/',views.logout),
    
    
]