from django.contrib import admin

# Register your models here.
from home.models import *

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Restaurant)
admin.site.register(Restaurant_user)
admin.site.register(Restaurant_appointment)
admin.site.register(Salon)
admin.site.register(Salon_user)
admin.site.register(Salon_appointment)
