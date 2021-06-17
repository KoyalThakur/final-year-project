from django.forms import formsets
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact,  Vendor, Property
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import auth
from home.forms import SignUpForm, PropertyForm
from django.urls import reverse_lazy



def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, desc=desc, date=datetime.today())
        contact.save()
    return render(request,'contact.html')

def signin(request):
    loginname = request.POST.get('loginname')
    loginpassword = request.POST.get('loginpassword')
    user = authenticate(request, username=loginname, password=loginpassword)
    if user is not None:
        login(request, user)
        return redirect('/listings')
    else:
         return render (request,'signIn.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def searchResult(request):
    return render(request, 'searchResult.html')

    
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            vendor= Vendor.objects.create(name=user.username,created_by=user)
            return redirect('/listings')
    else:
        form = SignUpForm()
    return render(request, 'signUp.html', {'form': form})

def list_view(request):
    vendor=request.user.vendor
    properties=vendor.properties.all()
    return render(request,'listings.html',{'vendor':vendor, 'properties':properties})

def add_property(request):
    if request.method=='POST':
        form=PropertyForm(request.POST,request.FILES)
        if form.is_valid():
            i=form.save(commit=False)
            i.vendor=request.user.vendor
            i.save()
            return redirect('/listings')
    else:
        form=PropertyForm()
    return render (request,'add.html',{'form':form})