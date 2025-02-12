from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('contact/',views.contact,name='contact'),
    path('team/',views.team,name='team'),
    path('base/',views.base,name='base'),
    path('register/',views.user_register,name='user_register'),
    path('user_login/',views.user_login,name='user_login'),
    path('logout/', views.user_logout,name="user_logout"),
    path('appointment/', views.appointment,name="appointment"),
    
]
