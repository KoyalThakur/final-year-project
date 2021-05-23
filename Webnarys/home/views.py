from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib.auth.models import User

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
def signIn(request):
    return render(request,'signIn.html')
def searchResult(request):
    return render(request, 'searchResult.html')   
def signUphandle(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        myuser=User.objects.create_user(name,email,password)
        myuser.save()
        return redirect('/index')

    else: 
         return HttpResponse("404 Error")


        