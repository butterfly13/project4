from django.shortcuts import render, redirect
from .models import Profile, Product, Message
from .forms import ProductForm, SignUpForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .forms import ArtistForm, SongForm

from django.contrib.auth import logout as site_logout
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

# Create your views here.


# Sign up 
def sign_up(request):
    if request.method == 'POST':
        # form = Form(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db() #load the profile instance created by the signal
            user.profile.address = form.cleaned_data.get('address')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.state = form.cleaned_data.get('state')
            user.profile.zipcode = form.cleaned_data.get('zipcode')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('product_list')
    else:
        # form = UserCreationForm()
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

# List of products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'sellnbuy/product_list.html', {'products': products})

# Detail of each product
def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'sellnbuy/product_detail.html', {'product': product})


# Add new product
@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    
    return render(request, 'sellnbuy/product_form.html', {'form': form})

#  Edit product
@login_required
def product_edit(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'sellnbuy/product_form.html', {'form': form})




