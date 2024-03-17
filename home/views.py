from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.views.decorators.cache import never_cache

from django.http import HttpResponse

def base(request):
  return render(request,'base.html') 


def user_register(request): 
    if request.method=="POST":
        fullname = request.POST.get('fullname')
        mobile = request.POST.get('mobile')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.create_user(username=username, password=password)
        user.fullname = fullname  
        user.mobile = mobile  
        
        user.save()
    return render(request,'user_register.html')
@never_cache
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request,'index.html')
        else:
            
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('user_register')  
    else:
        return render(request, 'user_register.html')

def user_logout(request):
    logout(request)
    return redirect('/')




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

def appointment(request):
  return render(request,'appointment.html')   



    