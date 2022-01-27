
from re import T
from unicodedata import name
from django.shortcuts import render
from django.template import context
from .models import MySkills,ContactItems



# Create your views here.

def home(request):

    item = MySkills.objects.all()

    title = 'Welcome to Here!'
    desc = 'Hello Sir, We are here to provide you all the services of software development...'

    context={

        'title':title, 
        'desc':desc,
        'item':item

    }

    return render(request,'index.html',context)

def about(request):
    title = 'About Us'
    desc = 'Do you know about us? 4axiz IT Ltd is the best web design and development company in Bangladesh and it also the one-off solutions for your technological enhancements in this global digitalized market which can provide you with an easier life than an analog world.We are prompt and creative software developers and IT engineers with excellent practical knowledge on all sort of website development, app development, customized CMS, templates and custom designs and any kind of software design & development whatever may suit your business needs.'

    context = {
        'title' : title,
        'desc' : desc
    }

    return render(request,'about.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('query')


        contact = ContactItems()

        contact.cname = name
        contact.cemail = email
        contact.cquery = query

        contact.save()

    return render(request,'contact.html')

