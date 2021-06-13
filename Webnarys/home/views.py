from django.forms import formsets
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact, Property
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import auth
from home.forms import SignUpForm, PropertyFormset

from django.views.generic import ListView, TemplateView
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
        return redirect('/')
    else:
         return render (request,'signIn.html')
 

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

#View for property list
class PropertyListView(ListView):
    model= Property
    template_name= "listings.html"

#View for adding property
class PropertyAddView(TemplateView):
    template_name= "add.html"
    def get(self, *args, **kwargs):
        formset= PropertyFormset(queryset=Property.objects.none())
        return self.render_to_response({'property_formset': formset})
    
    def post(self, *args, **kwargs):
        formset= PropertyFormset(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("listings"))
        return self.render_to_response({'property_formset': formset})

    
    