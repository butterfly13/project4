from django.shortcuts import render, redirect
from .models import Profile, Product, Message, State
from .forms import ProductForm

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .forms import ArtistForm, SongForm

# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required


# Create your views here.
# List of products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'sellnbuy/product_list.html', {'products': products})

# Detail of each product
def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'sellnbuy/product_detail.html', {'product': product})

# Add new product
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




