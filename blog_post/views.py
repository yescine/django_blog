from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import UserPost
from .form import BlogPostForm

def blog_post_detail(req):
   qs = UserPost.objects.all()
   context = {"object": qs}
   return render(req,"blogPostDetail.html",context)

def blog_post_page(req,post_id):
   obj = UserPost.objects.get(id=post_id)
   context = {"object": obj}
   return render(req,"blogPost.html",context)

@login_required
def blog_post_create(req):
   form=BlogPostForm(req.POST)
   if form.is_valid():
      print(form.cleaned_data)
      UserPost.objects.create(**form.cleaned_data)
      form=BlogPostForm()        
   context={"form":form}
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
