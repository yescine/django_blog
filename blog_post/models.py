from django.db import models

# Create your models here.
class UserPost( models.Model):
   title = models.TextField()
   contents=models.TextField(null=True,blank=True)

   def get_absolute_url(self):
      return f"/blog/{self.pk}/"

   def get_edit_url(self):
      return f"/blog/{self.pk}/edit/"

   def get_delete_url(self):
      return f"/blog/{self.pk}/delete/"