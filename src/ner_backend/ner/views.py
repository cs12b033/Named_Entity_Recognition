from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect
from django.conf import settings


# Create your views here.
def index(request):
    template = loader.get_template('ner/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def process(request):

    return
