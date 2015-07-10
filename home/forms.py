from django import forms
from django.forms import ModelForm
from .models import User,ShippingAddress



class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(metaForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'someClass'

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
       	   fields=['fullName','addressLine_1','addressLine_2','town','stateName','pinCode','countaryName','mobileNo','additionalAddress']
        		        