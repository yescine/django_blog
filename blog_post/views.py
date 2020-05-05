from django.shortcuts import render

# Create your views here.
from .models import UserPost

def blog_post_detail(req):
   qs = UserPost.objects.all()
   context = {"object": qs}
   return render(req,"blogPostDetail.html",context)

def blog_post_page(req,post_id):
   obj = UserPost.objects.get(id=post_id)
   context = {"object": obj}
   return render(req,"blogPost.html",context)

def blog_post_create(req):
   obj=None
   context={"from":obj}
   template_name= "blogPostCreate.html"
   return render(req,template_name,context)

def blog_post_update(req,post_id):
   obj=UserPost.objects.get(id=post_id)
   context={"object":obj,"from":None}
   template_name="blogPostUpdate.html"
   return render(req,template_name,context)

def blog_post_delete(req,post_id):
   obj=None
   context={"from":obj}
   template_name="blogPostDelete.html"
   return render(req,template_name,context)
