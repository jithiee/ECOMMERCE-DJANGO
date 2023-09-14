

from django.db import models
from django.contrib.auth import get_user_model
from Home.models import Vehicle
from accounts.models import Account

# User = get_user_model()

class BookingCar(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    car = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    picking_date = models.DateField()
    return_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user}"

    

class PaymentDetails(models.Model):
    razor_payment_id = models.CharField(max_length=255)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    booking = models.ForeignKey(BookingCar,on_delete=models.CASCADE)
    amount_paid = models.CharField(max_length=100) # this is the total amount
    razor_pay_status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.razor_payment_id)


    
    
    
    
    
    


    