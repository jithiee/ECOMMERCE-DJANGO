from django.db import models
# Create your models here.


class Vehicle(models.Model):
    # MAKE_CHOICES= [
    #     ('Toyota', 'Toyota'),
    #     ('Honda', 'Honda'),
    #     ('Ford', 'Ford'),
    #     ('Chevrolet', 'Chevrolet'),
    #     ('Nissan', 'Nissan'),
    #     ('BMW', 'BMW'),
    #     ('Mercedes-Benz', 'Mercedes-Benz'),
    #     ('Audi', 'Audi'),
    #     ('Volkswagen', 'Volkswagen'),
    #     # Add more brands here
    # ]

    def __str__(self):
        return f"{self.year} {self.make} - {self.transmission}"
    
    TRANSMISSION_CHOICES = [
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
        # ('CVT', 'CVT'),
      
    ]
    
    FUEL_TYPE = [
        ('Diesel','Diesel'),
        ('Petrol','Petrol'),
        ('Electric','Electric')
    ]
    
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField() 
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    car_img = models.ImageField(upload_to='vehicle_images/')  
    price = models.IntegerField(default=0) 
    is_available = models.BooleanField(default=True)
    description = models.TextField(max_length=500, blank=True)
    color = models.CharField(max_length=25)
    fuel = models.CharField(max_length=25,choices=FUEL_TYPE)
    
    

    

    def __str__(self):
        return f"  {self.make}   {self.transmission} {self.year} "
    

    
    
    
 