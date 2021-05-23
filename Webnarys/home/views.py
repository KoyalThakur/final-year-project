from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib.auth import login, authenticate
from home.forms import SignUpForm
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
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signUp.html', {'form': form})
    
    
    # def signUphandle(request):
#     if request.method == 'POST':
#         username=request.POST['username']
#         useremail=request.POST['useremail']
#         userpassword=request.POST['userpassword']
#         myuser=User.objects.create_user(username,useremail,userpassword)
#         myuser.save()
#         return redirect('/index')

#     else: 
#          return HttpResponse("404 Error")
        

        