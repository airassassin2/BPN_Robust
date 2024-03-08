from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('contact/',views.contact,name='contact'),
    path('team/',views.team,name='team'),
    path('register/',views.register,name='register'),
    path('base/',views.base,name='base'),
    path('login1/',views.login1,name='login1'),
    
]
