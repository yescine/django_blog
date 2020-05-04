from django.http import HttpResponse
from django.shortcuts import render

def welcome_page(req):
   parag = "some content"
   return render(req,"welcome.html",{"content":parag})  

def about_page(req):

   return HttpResponse("<h1>About </h1>")

def contact_page(req):
   
   return render(req,"contact.html")   