from django.db import models
from django.conf import settings

User=settings.AUTH_USER_MODEL
# Create your models here.
class UserPost( models.Model):
   title = models.TextField()
   contents=models.TextField(null=True,blank=True)
   user  = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
   publishDate=models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
   timestamp=models.DateTimeField(auto_now_add=True)
   updated=models.DateTimeField(auto_now=True)

   def get_absolute_url(self):
      return f"/blog/{self.pk}/"

   def get_edit_url(self):
      return f"/blog/{self.pk}/edit/"

   def get_delete_url(self):
      return f"/blog/{self.pk}/delete/"