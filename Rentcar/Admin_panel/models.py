from django.db import models
from Home.models import Vehicle

# Create your models here.
class car_income(models.Model):
    cars = models.ForeignKey(Vehicle,on_delete = models.SET_NULL,null=True)
    total_bookings = models.IntegerField()
    total_paid = models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True)
    last_payment_date = models.DateField(null=True,blank=True)
    pending_payment = models.DecimalField(max_digits=10,decimal_places=2)