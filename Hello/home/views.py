from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    context = {
        'variable1':"madarchod h",
        'variable2': "BSDK h"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("hello guys, this is my website")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("hello guys, this is about page")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'your message has been sent. We will contact you in 24 hours.')
    return render(request, 'contact.html')
    #return HttpResponse("hello guys, this is contact page")

def location(request):
    return render(request, 'location.html')
    #return HttpResponse("hello guys, this is location page")


# Create your views here.
