from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("homepage")

def blogs(request):
    return HttpResponse("BLOGS")

def blog_details(request,id):
    return HttpResponse("blog details"+id)