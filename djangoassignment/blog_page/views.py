from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import Myform
from .models import Blogs
from django.core.files.storage import FileSystemStorage


def blog_page(request):
    if request.method == 'GET':
        data = Blogs.objects.all()
        return render(request, 'form_blog.html', {'data': data[::-1]})
    else:  # post
        form = Myform(request.POST, request.FILES)
        print(request.POST, request.FILES)
        if form.is_valid():
            print(request.POST)
            file_obj = request.FILES['user_file']
            fs = FileSystemStorage()
            filename = fs.save(file_obj.name, file_obj)
            form.save()
            print(form.cleaned_data)
            return render(request, 'submitted.html', {})
        else:
            print('Could not be validated')
            return render(request, 'form_post_blog.html', {'form': form})





