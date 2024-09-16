from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from home.models import *
from django.http import HttpResponse


def base(request):
    return render(request, "base.html")


def base1(request):
    return render(request, "base1.html")


# @send_mail
def user_register(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        mobile = request.POST.get("mobile")
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if a user with the provided username already exists
        existing_user = User.objects.filter(username=username)

        if existing_user:
            # login(request, existing_user)
            messages.success(request, "User already register .")
            return redirect(
                "user_register"
            )  # Redirect to the index page after successful login

        else:
            # Create a new user
            user = User.objects.create_user(username=username, password=password)
            user.full_name = fullname
            user.mobile = mobile
            user.save()

            # Log in the newly created user
            login(request, user)
            messages.success(request, "Account created and logged in successfully.")
            return redirect(
                "index"
            )  # Redirect to the index page after successful creation and login

    # Render the registration form template for GET requests
    return render(request, "user_register.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successfull.")
            return render(request, "index.html")

        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect("user_register")
    else:
        return render(request, "user_register.html")


def user_logout(request):
    logout(request)
    return redirect("/")


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def service(request):
    return render(request, "service.html")


def team(request):
    return render(request, "team.html")


def contact(request):
    return render(request, "contact.html")


def profile(request):
    return render(request, "profile.html")


def setting(request):
    return render(request, "setting.html")


def notification(request):
    return render(request, "notification.html")


def appointment_form_modal(request):
    return render(request, "appointment_form_modal.html")
def restaurant_appointment(request):
    return render(request, "restaurant_appointment.html")
def salon_appointment(request):
    return render(request, "salon_appointment.html")
def dash_appointment(request):
    return render(request, "dash_appointment.html")


# def appointment(request):
#   doc=Doctor.objects.all()
#   return render(request,'appointment.html',{'doc': doc})


def dashboard(request):
    doctors = Appointment.objects.all().order_by("id").reverse()
    restaurant_name = Restaurant_appointment.objects.all().order_by("id").reverse()
    salon = Salon_appointment.objects.all().order_by("id").reverse()

    return render(
        request,
        "dashboard.html",
        {"doctors": doctors, "restaurant_name": restaurant_name, "salon": salon},
    )


def calender(request):
    return render(request, "calendar.html")


def adminpanel(request):
    doctors = Appointment.objects.all().order_by("id").reverse()
    return render(request, "adminpanel.html", {"doctors": doctors})


def appointment(request):
    if request.method == "POST":
        doctor_name = request.POST.get("doctor")
        patient_name = request.POST.get("name")
        date = request.POST.get("date")
        time = request.POST.get("time")

        # Check if the Doctor and Patient instances exist
        try:
            doctor = Doctor.objects.get(doctor_name=doctor_name)
            patient, created = Patient.objects.get_or_create(patient_name=patient_name)

        except ObjectDoesNotExist:
            return render(
                request,
                "appointment.html",
                {"message": "Doctor or Patient does not exist"},
            )

        # Create and save the Appointment instance
        appointment = Appointment(
            patient=patient, doctor=doctor, appointment_date=date, appointment_time=time
        )
        appointment.save()
        messages.success(request, "Appointment for Doctor booked successfully.")

        return redirect("appointment")
    doctors = Doctor.objects.all()
    return render(request, "appointment.html", {"doctors": doctors})

def restaurant_appointment(request):
    if request.method == "POST":
        doctor_name = request.POST.get("doctor")
        patient_name = request.POST.get("name")
        date = request.POST.get("date")
        time = request.POST.get("time")

        # Check if the Doctor and Patient instances exist
        try:
            doctor = Restaurant.objects.get(restaurant_name=doctor_name)
            patient, created = Restaurant_user.objects.get_or_create(name=patient_name)

        except ObjectDoesNotExist:
            return render(
                request,
                "restaurant_appointment.html",
                {"message": "Restaurant or User does not exist"},
            )

        # Create and save the Appointment instance
        appointment = Restaurant_appointment(
            name=patient, restaurant_name=doctor, appointment_date=date, appointment_time=time
        )
        appointment.save()
        messages.success(request, "Appointment for restaurant booked successfully.")

        return redirect("restaurant_appointment")
    doctors = Restaurant.objects.all()
    return render(request, "restaurant_appointment.html", {"doctors": doctors})

def salon_appointment(request):
    if request.method == "POST":
        doctor_name = request.POST.get("doctor")
        patient_name = request.POST.get("name")
        date = request.POST.get("date")
        time = request.POST.get("time")

        # Check if the Doctor and Patient instances exist
        try:
            doctor = Salon.objects.get(salon_name=doctor_name)
            patient, created = Salon_user.objects.get_or_create(name=patient_name)

        except ObjectDoesNotExist:
            return render(
                request,
                "salon_appointment.html",
                {"message": "Salon or User does not exist"},
            )

        # Create and save the Appointment instance
        appointment = Salon_appointment(
            name=patient, salon_name=doctor, appointment_date=date, appointment_time=time
        )
        appointment.save()
        messages.success(request, "Appointment for salon booked successfully.")

        return redirect("salon_appointment")
    doctors = Salon.objects.all()
    return render(request, "salon_appointment.html", {"doctors": doctors})




def appointment_form_modal(request):
    if request.method == "POST":
        # Extract data from the form
        appointment_type = request.POST.get("appointmentType")
        doctor_name = request.POST.get("doctor")
        patient_name = request.POST.get("name")
        date = request.POST.get("date")
        time = request.POST.get("time")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        gender = request.POST.get("gender")
        
        # Handle different types of appointments
        if appointment_type == "doctor":
            try:
                doctor = Doctor.objects.get(doctor_name=doctor_name)
            except Doctor.DoesNotExist:
                return render(
                    request,
                    "appointment_form_modal.html",
                    {"message": "Doctor does not exist"},
                )

            patient, created = Patient.objects.get_or_create(
                patient_name=patient_name, email=email, mobile=mobile, address="", gender=gender
            )

            appointment = ModalAppointment(
                patient=patient, doctor=doctor, appointment_date=date, appointment_time=time
            )
            appointment.save()
        elif appointment_type == "restaurant":
            # Handle restaurant appointment logic here
            # Example: Create RestaurantUser instance, etc.
            pass
        elif appointment_type == "salon":
            # Handle salon appointment logic here
            # Example: Create SalonUser instance, etc.
            pass

        return redirect("appointment_form_modal")

    doctors = Restaurant.objects.all()
    restaurants = Restaurant.objects.all()
    salons = Salon.objects.all()
    return render(request, "appointment_form_modal.html", {"doctors": doctors, "restaurants": restaurants, "salons": salons})



def sendemailtoclient():
    subject = "Message testing of email from Perwez"
    messages = "Testing for the reminder for Appointment"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["kjflajf@gmail.com"]
    send_mail(subject, messages, from_email, recipient_list)


def send_email(request):
    sendemailtoclient()
    return redirect("/")
