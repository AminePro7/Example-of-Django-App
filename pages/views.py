from django.shortcuts import render
from .models import Login
#from django.http import HttpResponse
# Create your views here.


def index(request):
   # return HttpResponse('This is an Index Page ')
   x={
       'Name':'Amine',
       'Age':21,
       'Country':'Tunisia'
   }
   return (render(request,'pages/index.html',x))

def about(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        data=Login(username=username,password=password)
        data.save()
    return (render(request,'pages/about.html'))

