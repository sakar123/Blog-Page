from django.urls import path
from .views import blog_page

urlpatterns =[
    path('home/', blog_page),
    path('home/post', blog_page)
]