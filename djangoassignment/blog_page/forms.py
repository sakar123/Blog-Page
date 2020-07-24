from django import forms
from .models import Blogs


class Myform(forms.ModelForm):
    author = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Full Name'})),
    blog = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"})),
    user_file = forms.FileField(widget=forms.FileInput(attrs={'class': "form-control"}))

    class Meta:
        model = Blogs
        fields = ('author', 'blog', 'user_file')









