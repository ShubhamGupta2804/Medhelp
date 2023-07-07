from django.shortcuts import render,redirect
from django.http import HttpResponse
from contact.models import contact
from django.contrib import messages


# Create your views here.

# def home(request):
#     return HttpResponse("medicine section")

def contact(request):

    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        city = request.POST['city']
        message = request.POST['message']

        cd = contact()
        cd.fname = fname
        cd.lname = lname
        cd.email = email
        cd.city = city
        cd.message = message
        cd.save()

        return redirect('home')
    return render(request,"authentication/contact.html")

# def __str__(self):
#     return self.fname