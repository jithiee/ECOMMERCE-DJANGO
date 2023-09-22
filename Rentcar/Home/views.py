from django.shortcuts import render,get_object_or_404
from .models import Vehicle
from Booking.models import BookingCar
from django.views.generic import View
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import date 

# Create your views here.



# def home(request):
#     search = request.GET.get('search','')
#     print(search)
    
#     Vehicles =Vehicle.objects.filter(is_available=True,make__icontains=search) 

#         # vehicles = Vehicle.objects.filter(make__icontains=search)
#     booked_cars = BookingCar.objects.all().values_list('car_id',flat=True)
#     # print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh',booked_cars)
    
#     for car in Vehicles:
#         print(car)
#         if car.id in booked_cars:
#             print('iiiiiiiiiiii',True)
    
    
#     context = {
#         'Vehicles':Vehicles,
#         'booked_cars':booked_cars,
        
#     }       
#     return render(request, 'home.html',context)


def home(request):
    search = request.GET.get('search', '')
    print(search)

    # Retrieve filter parameters from the request
    color_filters = request.GET.getlist('color')
    price_filters = request.GET.getlist('price')
    fuel_filters = request.GET.getlist('fuel')

    # Start with a queryset that includes all available vehicles
    Vehicles = Vehicle.objects.filter(is_available=True, make__icontains=search)

    # Apply color filters
    if color_filters:
        color_query = Q()
        for color_filter in color_filters:
            color_query |= Q(color=color_filter)
        Vehicles = Vehicles.filter(color_query)

    # Apply price filters
    if price_filters:
        price_query = Q()
        
        price_ranges = {
         
            '0 - 10000': (0, 10000),
           
            '10000 - 15000': (10000, 15000),
            '15000 - 20000': (15000, 20000),
            # '20000 <': (20000, float('inf')),
            '20000 - 100000': (20000,100000),
        }
        for price_filter in price_filters:
            min_price, max_price = price_ranges.get(price_filter, (0, 0))
            price_query |= Q(price__gte=min_price, price__lt=max_price)
        Vehicles = Vehicles.filter(price_query)

    # Apply fuel filters
    if fuel_filters:
        fuel_query = Q()
        for fuel_filter in fuel_filters:
            fuel_query |= Q(fuel=fuel_filter)
        Vehicles = Vehicles.filter(fuel_query)

    # Fetch the list of booked cars
    booked_cars = BookingCar.objects.all().values_list('car_id', flat=True)

    # Iterate over the filtered Vehicles and mark them as booked if their ID is in booked_cars
    for car in Vehicles:
        if car.id in booked_cars:
            car.is_booked = True
        else:
            car.is_booked = False

    context = {
        'Vehicles': Vehicles,
        'booked_cars': booked_cars,
    }
    

    return render(request, 'home.html', context)



def viewdetiles(request,car_id):
    cars = get_object_or_404(Vehicle,id=car_id)
    
    context = {
        'car':cars
    }
    return render (request,'viewdetiles.html',context)








# def search(request):
   
#         search = request.GET['search']
#         vehicles = Vehicle.objects.filter(make__icontains=search)
#         context = {
#             'vehicles': vehicles
#         }
#         return render(request, 'search.html', context)
    
    
    
    
    
  
def cars(request):
    Vehicles =Vehicle.objects.filter(is_available=True)   
    
    print('heloooooooooooooooooooooooooooooo')
    booked_cars = BookingCar.objects.all().values_list('car_id',flat=True)
    print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh',booked_cars)
    
    for car in Vehicles:
        print(car)
        if car.id in booked_cars:
            print('iiiiiiiiiiii',True)
    
    
    context = {
        'Vehicles':Vehicles,
        'booked_cars':booked_cars,
    }   
    return render(request, 'cars.html',context)

       
# @login_required(login_url = 'login')
def dashboard(request):
    usercar = BookingCar.objects.filter(user=request.user,return_date__gt=date.today())
    
    
    condext = {
        'usercar':usercar,
     
    }
    
    
    return render(request, 'dashboard.html',condext)      