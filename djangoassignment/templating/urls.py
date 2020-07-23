from django.urls import path
from .views import import_landing_page

urlpatterns = [
    path('base/', import_landing_page)
]