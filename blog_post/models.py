from django.db import models

# Create your models here.
class UserPost( models.Model):
   title = models.TextField()
   contents=models.TextField(null=True,blank=True)

