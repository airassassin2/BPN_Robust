from django.contrib import admin

# Register your models here.
from home.models import Patient,Doctor,Appointment

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
