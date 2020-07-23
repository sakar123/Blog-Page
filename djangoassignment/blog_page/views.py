from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import Myform
from .models import Blogs

def blog_page(request):
    if request.method == 'GET':
        data = Blogs.objects.all()
        return render(request, 'form_blog.html', {'data': data[::-1]})
    else: #post
        form = Myform(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return render(request, 'submitted.html', {})
        else:
            print('Could not be validated')
            return render(request, 'form_post_blog.html', {'form': form})





