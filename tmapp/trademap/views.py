from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from trademap.forms import AccountForm
from .models import Account, JobPostings
from .forms import AccountForm, JobForm
# Create your views here.

values = JobPostings.objects.all()

def index(request):
    return render(request, 'index.html',{
        'postings':values
    })


def make_post(request):
    return HttpResponse('make a post')


def post_details(request):
    return HttpResponse('more details')


def input_form(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('output_values')  # Redirect to output view
    else:
        form = JobForm()
    return render(request, 'input_form.html', {'form': form})


def output_values(request):  # Test function to output all objects from the database
    return render(request, 'output.html', {'values': values})


