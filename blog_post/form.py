from django import forms
from .models import UserPost
class BlogPostForm(forms.Form):
   title= forms.CharField(label="title here")
   contents= forms.CharField(widget=forms.Textarea, label="description")

   def clean_title(self,*args,**kwargs):
      title = self.cleaned_data.get('title')
      qs= UserPost.objects.filter(title=title)
      if qs.exists():
         raise forms.ValidationError("title already exist")
      return title

class UserPostModelForm(forms.ModelForm):
   class Meta:
      model=UserPost
      fields=['title','contents']