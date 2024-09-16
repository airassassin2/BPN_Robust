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
    path('restaurant_appointment/', views.restaurant_appointment,name="restaurant_appointment"),
    path('salon_appointment/', views.salon_appointment,name="salon_appointment"),
    path('base1/', views.base1,name="base1"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('adminpanel/', views.adminpanel,name="adminpanel"),
    path('calendar/', views.calender,name="calendar"),
    path('profile/', views.profile,name="profile"),
    path('setting/', views.setting,name="setting"),
    path('notification/', views.notification,name="notification"),
    path('appointment_form_modal/', views.appointment_form_modal,name="appointment_form_modal"),
    path('salon_appointment/', views.salon_appointment,name="salon_appointment"),
    path('restaurant_appointment/', views.restaurant_appointment,name="restaurant_appointment"),
    path('dash_appointment/', views.dash_appointment,name="dash_appointment"),
]
