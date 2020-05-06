
from django.urls import path
from .views import blog_post_page,blog_post_detail,blog_post_create,blog_post_update,blog_post_delete

urlpatterns = [
    path('',blog_post_detail), 
    path('<int:post_id>/',blog_post_page),
    path('<int:post_id>/edit/',blog_post_update), 
    path('<int:post_id>/delete/',blog_post_delete), 
]
