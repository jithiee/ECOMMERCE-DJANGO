
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CarBookingForms
from .models import BookingCar,PaymentDetails
from django.conf import settings
from Home.models import Vehicle
from django.urls import reverse
from django.shortcuts import get_object_or_404
import razorpay
from accounts.models import Account
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from Admin_panel.models import car_income
from datetime import date
from datetime import datetime

# def booking(request, car_id=None):
#         if car_id is not None:
#             try:
#                 vehicle = Vehicle.objects.get(id=car_id)
#             except Vehicle.DoesNotExist:
#                 return HttpResponse('Vehicle not found')

#         if request.method == 'POST':
            
#             pdate = request.POST.get('picking_date')
#             rdate= request.POST.get('return_date')
#             if date(pdate) < date.today():
#                 print('date must choose proprewplkejh')
#             elif date(pdate)>date(rdate):
#                 print('chose date properly')
#             else:
#                 vehicle = None
#                 forms = CarBookingForms(request.POST)
#                 try:
#                     vehicle = Vehicle.objects.get(id=car_id)
#                 except Vehicle.DoesNotExist:
#                     return HttpResponse('Vehicle not found')
#                 if forms.is_valid():

#                     booking = forms.save(commit=False)
#                     if request.user.is_authenticated:
#                         booking.user = request.user
#                         booking.car = vehicle
#                     else:
#                         pass

                    
#                     booking.save()

#                     return redirect('payment', book_id=booking.id)
#         else:
#             forms = CarBookingForms()
#         context = {
#             'form': forms,
#         }
#         return render(request, 'booking.html', context)



def booking(request, car_id=None):
    if car_id is not None:
        try:
            vehicle = Vehicle.objects.get(id=car_id)
        except Vehicle.DoesNotExist:
            return HttpResponse('Vehicle not found')

    if request.method == 'POST':
        pdate_str = request.POST.get('picking_date')
        rdate_str = request.POST.get('return_date')
        
        try:
            pdate = datetime.strptime(pdate_str, '%Y-%m-%d')
            rdate = datetime.strptime(rdate_str, '%Y-%m-%d')
        except ValueError:
            return HttpResponse('Invalid date format')

        if pdate < datetime.today():
            messages.error(request,' Picking date must be in the future')
        elif pdate > rdate:
            messages.error(request,'Return date must be after picking date')
        else:
            vehicle = None
            forms = CarBookingForms(request.POST)
            try:
                vehicle = Vehicle.objects.get(id=car_id)
            except Vehicle.DoesNotExist:
                return HttpResponse('Vehicle not found')
            if forms.is_valid():
                booking = forms.save(commit=False)
                if request.user.is_authenticated:
                    booking.user = request.user
                    booking.car = vehicle
                else:
                    pass

                booking.save()

                return redirect('payment', book_id=booking.id)
    forms = CarBookingForms()
    context = {
        'form': forms,
    }
    return render(request, 'booking.html', context)








def payment(request, book_id):
    print(book_id)
    forms = CarBookingForms()
    try:
        book=BookingCar.objects.get(id=book_id)
    except Exception as e:
        print(e)
    context = {
        'booking_id':book_id,
        'book': book,
        'amount':book.car.price,
        'form': forms,
    }
    return render(request, 'payment.html', context)





def success(request):
    print('hjdsagfdddddd')
    razorpay_payment_id = request.GET.get('razorpay_payment_id')
    print(razorpay_payment_id)
    book_id = request.GET.get('booking_id')
    print(book_id)
    # car_id = request.GET.get('car_id')
    booking = get_object_or_404(BookingCar,id=book_id)
    # print(car_id,book_id,razorpay_payment_id)


    
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY, settings.RAZORPAY_SECRET_KEY))



    try:
        payment = client.payment.fetch(razorpay_payment_id)

        amount_paid = payment['amount'] / 100  
        razor_pay_status = payment['status']
        print(razor_pay_status,amount_paid)

        PaymentDetails.objects.create(
            razor_payment_id=razorpay_payment_id,
            user=booking.user,  
            booking_id = booking.id,
            amount_paid=amount_paid,
            razor_pay_status=razor_pay_status
        )
        booking.is_paid = True
        booking.save()

    except razorpay.errors.BadRequestError as e:
        return HttpResponse(f'Error: {str(e)}')


    
    return render(request,'success.html')