from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
 
def index(request):
    return render(request,"index/home.html")

def about(request):
    return render(request,'index/about.html')

def contact(request):
    return render(request,'index/contact.html')