from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Home page')

def group_posts(request, slug):
    return HttpResponse(f'Group {slug}')
