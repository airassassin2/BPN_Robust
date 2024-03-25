from django.db import models
from django.contrib.auth.models import User


# class User(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     fullname=models.CharField(max_length=50)
#     mobile=models.CharField(max_length=10)
#     username=models.EmailField()
#     password=models.CharField(max_length=100)

#     def __str__(self):
#         return self.fullname



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