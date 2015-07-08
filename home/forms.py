from django import forms
from django.forms import ModelForm
from .models import User,ShippingAddress



# Create the form class.
class SignupForm(ModelForm):
   class Meta:
       model = User
       fields = ['firstName', 'lastName', 'emailId', 'contactNo','cityName','dateOfBirth','password','password']


class LoginForm(ModelForm):
    class Meta:
        model=User
        fields=['emailId','password','password']
    
class Shipping(ModelForm):
     class Meta:
       	   model=ShippingAddress
       	   fields=['fullName'] #,'addressLine_1','addressLine_2','town','stateName','pinCode','countaryName','mobileNo','additionalAddress']
        		        