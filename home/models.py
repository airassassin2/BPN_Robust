from django.db import models


class Doctor(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.IntegerField(max_length=10)
    speciality=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name



class Patient(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.IntegerField(max_length=10)
    address=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    appointment_date=models.DateField()
    appointment_time=models.TimeField()

    def __str__(self) -> str:
        return self.doctor.name+ " ---> " +self.patient.name
       