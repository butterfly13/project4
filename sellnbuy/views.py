from django.shortcuts import render
from .models import Profile, Product, Message, State

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .forms import ArtistForm, SongForm

# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'sellnbuy/product_list.html', {'products': products})