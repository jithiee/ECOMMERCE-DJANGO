from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
        'class' : 'form_control',
        
    }))
    conform_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'comform Password',
         'class' : 'form_control',
        
    }))
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'First name',
         'class' : 'form_control',
        
    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Last name',
         'class' : 'form_control',
        
    }))
    
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder':'Phone number',
         'class' : 'form_control',
        
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
          'placeholder':'Enter email',
         'class' : 'form_control',
    }))
    
    
    
    class Meta:
        model = Account
        fields = ['first_name','last_name','phone_number','email','password']
        
    def clean(self): 
       cleaned_data = super(RegistrationForm, self).clean()
       password = cleaned_data.get('password')
       conform_password = cleaned_data.get('conform_password')  # Corrected variable name here
       if password != conform_password:
             raise forms.ValidationError('Passwords do not match!')
            

        