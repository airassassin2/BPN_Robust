from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Permission


class Custom_User(AbstractUser):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField()
    fullname=models.CharField(max_length=100)
    # mobile = models.CharField(max_length=20)
    class Meta:
        db_table = 'home_auth_user'  
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='home_user_groups_unique')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'), blank=True, related_name='home_user_permissions_unique')



class Doctor(models.Model):
    doctor_name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    speciality=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.doctor_name



class Patient(models.Model):
    patient_name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)

    def __str__(self) -> str:
        return self.patient_name


class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    appointment_date=models.DateField()
    appointment_time=models.TimeField()

    def __str__(self) -> str:
        return self.doctor.doctor_name+ " ---> " +self.patient.patient_name
       



class Restaurant(models.Model):
    restaurant_name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    speciality=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.restaurant_name
    
class Restaurant_user(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)
    email=models.EmailField()


    def __str__(self) -> str:
        return self.name
    
    
class Restaurant_appointment(models.Model):
    restaurant_name=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    name=models.ForeignKey(Restaurant_user,on_delete=models.CASCADE)
    appointment_date=models.DateField()
    appointment_time=models.TimeField()


    def __str__(self) -> str:
        return self.restaurant_name.restaurant_name +" --> "+ self.name.name
        

class Salon(models.Model):
    salon_name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    speciality=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.salon_name


class Salon_user(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)
    email=models.EmailField()


    def __str__(self) -> str:
        return self.name

    
class Salon_appointment(models.Model):
    salon_name=models.ForeignKey(Salon,on_delete=models.CASCADE)
    name=models.ForeignKey(Salon_user,on_delete=models.CASCADE)
    appointment_date=models.DateField()
    appointment_time=models.TimeField()


    def __str__(self) -> str:
        return self.salon_name.salon_name +" --> "+ self.name.name
    










class ModalAppointment(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=(('male', 'Male'), ('female', 'Female'), ('other', 'Other')))
    
    # Define choices for booking types
    BOOKING_CHOICES = (
        ('doctor', 'Doctor'),
        ('salon', 'Salon'),
        ('spa', 'Spa'),
        ('corporate', 'Corporate'),
        ('government', 'Government'),
    )

    # Define foreign key fields with choices
    booking_type = models.CharField(max_length=20, choices=BOOKING_CHOICES)
    doctor_booking = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_appointments', null=True, blank=True)
    salon_booking = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name='salon_appointments', null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.fullname
    

class happy(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()

