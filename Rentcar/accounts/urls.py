
from django.urls import path
from .import views



urlpatterns = [

    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    
    path('activate/<uidb64>/<token>/',views.activate,name ='activate' ),
      
    path('foregotpassword/',views.foregotpassword,name='foregotpassword'),
    path('resetpassword_validate/<uidb64>/<token>/',views.resetpassword_validate,name ='resetpassword_validate' ),
    path('resetpassword/',views.resetpassword,name='resetpassword')

]