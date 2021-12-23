from django.shortcuts import render
from .models import *

def index_view(request):


    return render(request,'index.html')


def about_view(request):
    return render(request,'about.html')


def contact_view(request):
    return render(request,'contact.html')

def property_single_view(request):
    return render(request,'property-single.html')

def property_grid_view(request):
    return render(request,'property-grid.html')

def blog_grid_view(request):
    return render(request,'blog-grid.html')

def blog_single_view(request):
    return render(request,'blog-single.html')

def agent_single_view(request):
    return render(request,'agent-single.html')

def agents_grid_view(request):
    return render(request,'agents-grid.html')

