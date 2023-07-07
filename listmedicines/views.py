from django.shortcuts import render,redirect
from django.http import HttpResponse
from listmedicines.models import List_medicines
from django.contrib import messages


# Create your views here.

def home(request):
    return HttpResponse("medicine section")

def list_medicines(request):

    if request.method=='POST':
        medname = request.POST['medname']
        quantity = request.POST['quantity']
        expiry = request.POST['expiry']

        med = List_medicines()
        med.medicineName = medname
        med.quantity = quantity
        med.expiry = expiry

        med.save()
        messages.success(request,'Medicine Listed Successfully!!!')
        return redirect('home')
    return render(request,"authentication/list_medicines.html")

def __str__(self):
    return self.medname