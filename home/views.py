from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout

from django.http import HttpResponse


def register(request): 
  if request.method=="POST":
    fullname=request.POST.get('fullname')
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=User.objects.create_user(username=username,password=password)
    user.fullname=fullname
    user.save()
  return render(request,'register.html')

def login(request):
  if request.method=="POST":
    username=request.POST.get('username')
    password=request.POST.get('password')

    if not User.objects.filter(username=username,password=password).exist():
      return redirect('login')
    user=authenticate(request,username=username, password=password)


def index(request):
  return render(request,'index.html')    
def about(request):
  return render(request,'about.html')    
def service(request):
  return render(request,'service.html')    
def team(request):
  return render(request,'team.html')    
def contact(request):
  return render(request,'contact.html')   

def base(request):
  return render(request,'base.html') 

    