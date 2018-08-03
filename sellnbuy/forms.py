from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Profile, Message
from django.forms import ModelChoiceField

class ProductForm(forms.ModelForm):
    
    profile = forms.ModelChoiceField(queryset=Profile.objects.all(), widget=forms.Select(), empty_label='--Pick Seller--')
   
    
    class Meta:
        model = Product
        fields = ('profile','product_name', 'description', 'qty', 'price', 'image','category', 'condition', )
         



class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=100, required=False, help_text='Require.')
    # last_name = forms.CharField(max_length=100, required=False, help_text='Require.')
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    # address = forms.CharField(max_length=100)
    # city = forms.CharField(max_length=100)
    # state = forms.CharField(max_length=100)
    # state = forms.ModelChoiceField(queryset=Product.objects.filter(type="profile"))
    # zipcode = forms.CharField(max_length=10)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','username', 'password1', 'password2',   )
       


