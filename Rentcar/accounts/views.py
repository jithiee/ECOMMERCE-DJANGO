from django.shortcuts import render,redirect
from . forms import RegistrationForm
from . models import Account
from django.contrib import messages,auth
from django.http import HttpRequest ,HttpResponse 
from django.contrib.auth.decorators import login_required


#verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.core.mail import EmailMessage
 


# Create your views here.
def register(request):
    if request.method =='POST':
      form =  RegistrationForm(request.POST)
     
      if form.is_valid():
            first_name = form.cleaned_data['first_name']
            # print( form.cleaned_data )
            # print(form.cleaned_data['first_name'])
          
            last_name = form.cleaned_data['last_name']
         
            phone_number = form.cleaned_data['phone_number']
         
            email = form.cleaned_data['email']
         
            password = form.cleaned_data['password']
            
            username = email.split('@')[0] 
            # print(username)
            
            user = Account.objects.create_user(first_name =first_name,last_name = last_name,email =email ,username=username )
            user.phone_number = phone_number
            user.set_password(password)
            user.is_active= False
            user.save()
            # print('1')
            
            #user activation 
            current_site = get_current_site(request)
            mail_subject = "please activate your account"  # Fixed typo here    
            # print('2')
            message = render_to_string('verification_email.html',{
               'user':user,
               'domain': current_site,
               'uid': urlsafe_base64_encode(force_bytes(user.pk)), #user id
               'token':default_token_generator.make_token(user),
            })
            # print('3')

            to_email = email
            sent_email = EmailMessage(mail_subject, message, to=[to_email])
            sent_email.send()  
            # print('4')
            
            messages.success(request,'Registration Successfull Check your email for further instructions')
            # return redirect('login')
    else:
        form = RegistrationForm()
    context = {'form':form}
   
    return render(request,'register.html',context)



def login(request):
    if request.method == 'POST':
        email = request.POST['email']  # name of input feild
        password = request.POST['password']  
        
        user =auth.authenticate(email = email , password = password )
        
        if user is not None:
            auth.login(request,user)
            # messages.success(request,'you are now logged in ')
            return redirect ('home')
        else:
            messages.error(request,'Invaid login.....!')
            return redirect ('login')
    return render(request,'login.html') 



@login_required(login_url = 'login')                  #first chech  if you are login you can logout if you are not login you can't logout
def logout(request):
    auth.logout(request)
    messages.success(request,'you are logged out')
    return redirect('login')
  
  
  # email activation 
def activate(request,uidb64,token):
   try :
       uid = urlsafe_base64_decode(uidb64).decode()
       print(uid)
       user =  Account.objects.get (pk = uid)
    #    print('jhjh',user)
   except (TypeError,ValueError,OverflowError,Account.DoesNotExist):
       user = None
   if user is not None and default_token_generator.check_token(user,token):
       user.is_active = True
       user.save()
       messages.success(request,'congratulaions your account  is activated') 
       return redirect('login')
   else:
       messages.error(request,'Invalid activation link') 
       return redirect('register')
    
    
    

# def login_need(view_func):
#     def wrapper(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return view_func(request, *args, **kwargs)
#         else:
#             return redirect('login')
#     return wrapper
   
    

# @login_need 
    



def foregotpassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email = email)# iexact caseseciteve
            
            #Reset password email
            current_site = get_current_site(request)
            mail_subject = "reset your password"  # Fixed type here
            print('2')
            message = render_to_string('resetpassword_email.html',{
               'user':user,
               'domain': current_site,
               'uid': urlsafe_base64_encode(force_bytes(user.pk)), #user id
               'token':default_token_generator.make_token(user),
            })
            print('3')

            to_email = email
            sent_email = EmailMessage(mail_subject, message, to=[to_email])
            sent_email.send() 
            
            messages.success(request,'passwod reset email has email your email address') 
            return redirect('login')

        else :
            messages.error(request,'Account doese not exist !') 
            return redirect ('foregotpassword')   
    
        
        
    return render (request, 'foregotpassword.html' )

def resetpassword_validate(request,uidb64,token):
    try :
       uid = urlsafe_base64_decode(uidb64).decode()
       print(uid)
       user =  Account.objects.get (pk = uid)
       print('jhjh',user)
    except (TypeError,ValueError,OverflowError,Account.DoesNotExist):
       user = None
    if user is not None and default_token_generator.check_token(user,token):
        request.session['uid']  = uid
        messages.success(request,'please reset your password')  
        return redirect('resetpassword')
    else :
        messages.error(request,'this link has be expierd')
        return redirect ('login')
    
def resetpassword(request):
    if request.method == "POST":
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password :
            uid = request.session.get('uid')
            user = Account.objects.get(pk = uid)
            user.set_password(password)
            user.save()
            messages.success(request,'password Rest succussful')
            return redirect('login')
        else:
            messages.error(request,'password do not match')
            return redirect('resetpassword')
    else:
       return render(request,'resetpassword.html')
            
        
        
 
           