from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def import_landing_page(request):
    template = loader.get_template('landing_page.html')
    context = {}
    template_data = template.render(context, request)
    return HttpResponse(template_data)

# Create your views here.
