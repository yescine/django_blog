from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
from .models import UserPost
from .form import BlogPostForm, UserPostModelForm

def blog_search(req):
   q=req.GET.get('query')
   obj=UserPost.objects.filter(title__icontains=q)
   context={"object":obj}
   template_name= "search.html"
   return render(req,template_name,context)

def blog_post_detail(req):
   qs = UserPost.objects.all()
   context = {"object": qs}
   return render(req,"blogPostDetail.html",context)

def blog_post_page(req,post_id):
   obj = UserPost.objects.get(id=post_id)
   context = {"object": obj}
   return render(req,"blogPost.html",context)

@staff_member_required
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
   form=UserPostModelForm(req.POST or None, instance=obj)
   if form.is_valid():
      form.save()
   context={"form":form,"title":obj.title}
   template_name="blogPostUpdate.html"
   return render(req,template_name,context)

@staff_member_required
def blog_post_delete(req,post_id):
   obj=UserPost.objects.get(id=post_id)
   if req.method=="POST":
      obj.delete()
      return redirect('/blog')
   context={"form":obj,"title":obj.title}
   template_name="blogPostDelete.html"
   return render(req,template_name,context)
