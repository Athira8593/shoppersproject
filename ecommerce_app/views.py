from admin_app.forms import AddressForm,UserForm,CheckoutForm
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, request
# Create your views here.
from.models import Product,Category
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from accounts.models import Account
from cart.models import Cart,CartItem,Buynow
from django.contrib import messages
from cart.views import _cart_id
from django.db.models import Q
from orders.models import DeliveryAddress
from django.views.decorators.cache import never_cache
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

def allproduct(request,c_slug=None):
    c_page=None
    products=None
    if c_slug==None:
        products=Product.objects.all().filter(available=True).order_by('-id')[:12]
        return render(request,'index.html',{'category':c_page,'products':products})
    else: 
        c_page = get_object_or_404(Category,slug=c_slug)
        products=Product.objects.filter(category=c_page,available=True).order_by('-id')
    return render(request,'product.html',{'category':c_page,'products':products})


def all_product(request,c_slug=None):

        products=Product.objects.all().filter(available=True).order_by('-id')
        return render(request,'all_product.html',{'products':products})



def single_view(request,c_slug,product_slug):
        try:
            products = Product.objects.get(category__slug=c_slug, slug=product_slug)
            # in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request),product=products).exists()
        except Exception as e:
            raise e
        return render(request, 'single_view.html', {'product': products})

def user_profile(request,id):
    if request.session.get('login') == True:
        user = Account.objects.get(id=id)
        return render(request, 'user/user_profile.html',{'user':user})
    else:
        return redirect('user_login')

def edit_profile(request,id):
    if request.session.get('login') == True:
        user = Account.objects.get(id=id)
        if request.method== 'POST':
            form=UserForm(request.POST,request.FILES, instance=user)
            
            if form.is_valid():
                form.save()
                return redirect('user_profile', id=id)
        else:
            form=UserForm(instance=user)
            return render(request,'user/update_profile.html',{'user':user,'form':form})
    else:
        return redirect('user_login')


def edit_address(request,id):
    if request.session.get('login') == True:
        address = Account.objects.get(id=id)
        if request.method== 'POST':
            form=AddressForm(request.POST, instance=address)
            print(form)
            if form.is_valid():
                form.save()
                return redirect('user_profile', id=id)
        else:
            form=AddressForm(instance=address)
            return render(request,'user/update_address.html',{'address':address,'form':form})
    else:
        return redirect('user_login')


def current_pass(request,id):
    if request.session.get('login') == True:
        if request.method== 'POST':
            password = request.POST.get('password')
            user = request.user.password
            print(user)
            print(password)
            if user == password:
                print(user)
                return redirect('change_password' ,id=id)
            else:
                return redirect('current_pass', id=id)
        else:
            return render(request, 'user/current_pass.html')
    else:
        return redirect('user_login')



def change_password(request,id):
    if request.session.get('login') == True:
        user = Account.objects.get(id=id)
        if request.method== 'POST':
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                user.save()
                return redirect('user_profile', id=id)
            else:
                return redirect('change_password')
        else:
            return render(request, 'user/change_password.html')
    else:
        return redirect('user_login')



def search(request):
    products = None
    query = None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__icontains=query) | Q(desc__icontains=query))
    
    return render(request,"search.html",{'query':query, 'products':products})


