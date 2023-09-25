from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from  Home.models  import   Vehicle
from .forms import Carforms
from django.contrib.auth.decorators import user_passes_test
# Create your views here.


def car_list(request):
    if request.user.is_superadmin:
        cars = Vehicle.objects.all()
        context = {'cars':cars}
        return render(request,'car_list.html',context)
    else:
        return redirect('home')




def car_upload_forms(request, car_id=0):
   if request.user.is_superadmin:
    if request.method == 'GET':
    
        if car_id == 0:
            form = Carforms()
        else:
            car = Vehicle.objects.get(pk=car_id)
           
            form = Carforms(instance=car)
        return render(request, 'car_upload_forms.html', {'form': form,'id':id})
  
   

    # Rest of your view logic for POST requests remains the same

    else:
        print('id-----------------',car_id)
        if car_id == 0:
            print('request is post')
            form = Carforms(request.POST,request.FILES) 
            print(form)
            print('id-----------------',car_id)
            if form.is_valid():
                form.save()
            else:
                print(form.errors)
            
        else:
            car  = Vehicle.objects.get(pk=car_id)   
            print(car)
            form = Carforms(request.POST,request.FILES,instance = car) 
            if form.is_valid():
                form.save()

            else:
                print(form.errors)
            
        
        return redirect('car_list')  
    
def car_delete(request, car_id):
    car = Vehicle.objects.get(pk = car_id)
    car.delete()
    return redirect('car_list')
         
def adminsearch(request ):
   
        search = request.GET['search']
        vehicles = Vehicle.objects.filter(make__icontains=search)
        context = {
            'vehicles': vehicles
        }
        return render(request, 'adminsearch.html', context)


   
def admin_access(request):
    if request.user.is_superadmin:
       return render(request,'admin_access.html')    
    else:
       return redirect('home')
    
   

               

   
    
    
