from django import forms
from django.contrib.auth.models import User
from . import models
from phonenumber_field.formfields import PhoneNumberField

class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile','profile_pic']

class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=['name','price','description','product_image','quantity']

#address of shipment
class AddressForm(forms.Form):
    Email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email',}))
    Mobile = PhoneNumberField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Phone Number'}))
    Address = forms.CharField(widget = forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address'}))

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['name','feedback']

#for updating status of order
class OrderForm(forms.ModelForm):
    class Meta:
        model=models.Orders
        fields=['status']

#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
