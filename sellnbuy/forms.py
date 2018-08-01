from django import forms
from .models import Product, Profile, Message, State

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('profile', 'product_name', 'description', 'qty', 'price', 'image', 'condition', 'category',)


# class SongForm(forms.ModelForm):
    
#     class Meta:
#         model = Song
#         fields = ('title', 'album', 'preview_url', 'artist',)