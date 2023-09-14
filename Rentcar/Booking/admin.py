from django.contrib import admin
from . models import *
from django.contrib.auth.admin import UserAdmin 



class BokkAdmin(admin.ModelAdmin):
    list_display=['id','user','picking_date','return_date']
    list_display_links=['id','user']
admin.site.register(BookingCar,BokkAdmin)

class PayAdmin(admin.ModelAdmin):
    list_display = ['razor_payment_id','user',]

admin.site.register(PaymentDetails,PayAdmin)





