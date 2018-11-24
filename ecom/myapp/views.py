from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.utils import timezone
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import *
from django.contrib.auth import authenticate, login, logout
import random
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
# Create your views here.

#
# def Getbase(request):
#     cat = Category.objects.all()
#     sub_cat = SubCategory.objects.all()
#     brand = Brand.objects.all()
#     return render(request, 'base.html', {'cat': cat,"sub_cat":sub_cat,"brand":brand})
# def commensection(request):
    # com = Comment.objects.all()
    # sub_cat = SubCategory.objects.all()
    # if request.user.is_authenticated:
    #     use = get_object_or_404(User, id=request.user.id)
    #     car = cart.objects.filter(customer=use.id)
    # else:
    #     car=''
#     com_con={
#             "sub_cat":sub_cat,"cart":car,"com":com    }
#     return com_con


def getindex(request):
    contact_list = Product.objects.filter(created_date__lte=timezone.now()).order_by('?') # ? dila ata ramdom data nia kaj kora
    # contact_list = Product.objects.filter(created_date__lte=timezone.now()).order_by('-created_date') # R ata date nia kaj kora
    search = request.GET.get('q')
    if search:
        contact_list=contact_list.filter(
            Q(product_model__icontains=search)|
            Q(brand__name__icontains=search)|
            Q(sub_cat__name__icontains=search)|
            Q(cat_name__cat_name__icontains=search)
        )
    if not contact_list:
        messages.error(request,f'Not Found any product ({search}) please try again letter')
    sub_cat = SubCategory.objects.all()
    if request.user.is_authenticated:
        use = get_object_or_404(User, id=request.user.id)
        car = cart.objects.filter(customer=use.id)
    else:
        car=''
    paginator = Paginator(contact_list, 6) # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    com = Comment.objects.all()
    contex={
            'contacts': contacts,"sub_cat":sub_cat,"cart":car,"com":com
        }
    return render(request, 'index.html',contex)

def getcategory(request, name):
    sub_cat = SubCategory.objects.all()
    post = get_object_or_404(SubCategory, name=name)
    contex = Product.objects.filter(sub_cat=post.id)
    brand = Brand.objects.filter(sub_cat=post.id)
    if request.user.is_authenticated:
        use = get_object_or_404(User, id=request.user.id)
        car = cart.objects.filter(customer=use.id)
    else:
        car=''
    contex={
            "contex":contex,"brand":brand,"sub_cat":sub_cat,"cart":car
        }
    return render(request,'laptop.html',contex)

def Getbrand(request, name):
    sub_cat = SubCategory.objects.all()
    post = get_object_or_404(Brand, name=name)
    contex = Product.objects.filter(brand=post.id)
    brand = Brand.objects.filter(sub_cat=post.sub_cat)
    if request.user.is_authenticated:
        use = get_object_or_404(User, id=request.user.id)
        car = cart.objects.filter(customer=use.id)
    else:
        car=''
    contex ={"contex":contex,"brand":brand,"sub_cat":sub_cat,"cart":car}
    return render(request,'laptop.html',contex)


def Getregister(request):
    sub_cat = SubCategory.objects.all()
    forms = Registration(request.POST or None)
    cus_form = Reg_cus(request.POST or None)
    contex={"forms":forms, "cus_form":cus_form,"sub_cat":sub_cat}
    if forms.is_valid() and cus_form.is_valid():
        user=forms.save()
        done = cus_form.save(commit=False)
        done.name=user
        done.save()
        messages.success(request,'Registration Successfull!:)')
        return redirect('index')
    return render(request,'register.html',contex)

def GetLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(request, username=username, password=password)
        if auth is not None:
            login(request, auth)
            messages.success(request, 'Login Succesfull..Welcome to our ecom page:)')
            return redirect('index')
        else:
            return redirect('register')

def Getlogout(request):
    logout(request)
    messages.error(request, 'You are now logout!')
    return redirect('index')


def Getproduct_details(request, id):
    sub_cat = SubCategory.objects.all()
    contex = Product.objects.get(id=id)
    com = Comment.objects.filter(product=contex.id)
    if request.user.is_authenticated:
        use = get_object_or_404(User, id=request.user.id)
        car = cart.objects.filter(customer=use.id)
    else:
        car=''
    contex={"con":contex,"sub_cat":sub_cat,"com":com,"cart":car}
    return render(request, 'details.html',contex)

def Getpays(request, id):
    if request.user.is_authenticated:
        contex = Product.objects.get(id=id)
        sub_cat = SubCategory.objects.all()
        if request.user.is_authenticated:
            use = get_object_or_404(User, id=request.user.id)
            car = cart.objects.filter(customer=use.id)
        else:
            car=''
        contex = {"con":contex,"sub_cat":sub_cat,"cart":car}
        return render(request, 'payc.html',contex,{})
    return redirect('register')

def Getcomment(request,id):
    pro_ins = get_object_or_404(Product, id=id)
    if request.user.is_authenticated:
        contex = Product.objects.get(id=id)
        sub_cat = SubCategory.objects.all()
        if request.user.is_authenticated:
            use = get_object_or_404(User, id=request.user.id)
            car = cart.objects.filter(customer=use.id)
        else:
            car=''
        if request.method == 'POST':
            commentaa = request.POST.get('comment')
            ratingaa = request.POST.get('star')
            if commentaa is not None and ratingaa is not None:
                post=Comment()
                post.product=pro_ins
                post.customer = request.user
                post.comment = request.POST.get('comment')
                post.rating = request.POST.get('star')
                post.save()
                post.calculate_rating(id=id)
                return redirect('product_details',id=id)
            else:
                messages.error(request,"Please Give your rating and comment:)")
        contex = {"con":contex,"sub_cat":sub_cat,"cart":car}
        return render(request, 'rating.html',contex)




def Getcart(request, id,name):
    pro_ins = get_object_or_404(Product, id=id)
    car=cart()
    car.customer=request.user
    car.product=pro_ins
    car.save()
    messages.info(request,"Product add on your cart:-))")
    if name == 'add':
        # return render(request,'cart.html')
        return redirect('gocart', id=request.user.id)
    return redirect('product_details', id=id)

def Getgocart(request, id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=id)
        cart_all = cart.objects.filter(customer=user.id)
        total=0
        for cc in cart_all:
            total += cc.product.prince
        contex={"cart":cart_all,"total":total}
        return render(request,'cart.html',contex)
    else:
        return redirect('index')

def Getcartdelete(request,id):
    if request.user.is_authenticated:
        item=get_object_or_404(cart, id=id)
        uid=item.customer.id
        item.delete()
        messages.success(request,"Product Remove Successfull:)")
        return redirect('gocart',id=uid)
    else:
        return redirect('index')
