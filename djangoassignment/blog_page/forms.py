from django import forms
from .models import Blogs

class Myform(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['author', 'blog']





