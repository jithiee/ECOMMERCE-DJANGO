from django.urls import path
from . import views

urlpatterns = [
    path('booking/<int:car_id>/', views.booking, name='booking'),
    path('payment/<int:book_id>/', views.payment, name='payment'),
    path('success/', views.success, name='success')

]
