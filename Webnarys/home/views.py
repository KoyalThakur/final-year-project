from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def signIn(request):
    return render(request,'signIn.html')
def searchResult(request):
    return render(request, 'searchResult.html')    