from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def authenticate(request):
    return HttpResponse("poggers")


def load_home(request):
    return HttpResponse('home')


def make_post(request):
    return HttpResponse('make a post')


def post_details(request):
    return HttpResponse('more details')
