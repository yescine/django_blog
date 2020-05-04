from django.http import HttpResponse
from django.shortcuts import render

def welcome_page(req):
   parag = "some content"
   context={"content":parag}
   return render(req,"welcome.html",context)  

def about_page(req):

   return HttpResponse("<h1>About </h1>")

def contact_page(req):
   
   return render(req,"contact.html")   

def example_page(req):
   context={"content":"example type content for tags","list":["one","two","three"]}
   return render(req,"example.html",context) 