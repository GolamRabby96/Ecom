from .models import Customer
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Registration(UserCreationForm):
    class Meta:
        model = User
        fields =[
            'first_name','last_name','email','username','password1','password2'
        ]

        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Last Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Your Email'}),
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Username'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Your Password'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Your Password'})
        }


class Reg_cus(forms.ModelForm):
    class Meta:
        model = Customer
        fields=[
            'phone','locations'
        ]
        widgets={
            'phone':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Your Phone Number'}),
            'locations':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Your Locations Details'}),
        }
