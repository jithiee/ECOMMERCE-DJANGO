
from django.urls import path
from .import views



urlpatterns = [


    path('car_insert/', views.car_upload_forms, name='car_insert'),  
    path('car_update/<int:car_id>/',views.car_upload_forms,name='car_update'),
    path('car_list/',views.car_list,name='car_list'),
    path('car_delete/<int:car_id>/',views.car_delete,name='car_delete'),
    path('adminsearch/',views.adminsearch,name='adminsearch'),
    path('admin_access/',views.admin_access,name="admin_access"),
    
 ]