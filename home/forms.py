from django import forms
from django.forms import ModelForm
from .models import User



# Create the form class.
class SignupForm(ModelForm):
   class Meta:
       model = User
       fields = ['firstName', 'lastName', 'emailId', 'contactNo','cityName','password','password']


class LoginForm(ModelForm):
    class Meta:
        model=User
        fields=['emailId','password','password']
    
        