from django.shortcuts import render

# Create your views here.
from .models import UserPost

def blog_post_page(req,post_id):
   obj = UserPost.objects.get(id=post_id)
   context = {"object": obj}
   return render(req,"blogPost.html",context)