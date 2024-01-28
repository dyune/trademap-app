from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from trademap.forms import AccountForm
from .models import Account, JobPostings
from .forms import AccountForm, JobForm
# Create your views here.


values = JobPostings.objects.all()


def index(request):
    len(values)
    
    return render(request, 'index.html', {
        'postings': values
    })


def input_form(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to output view
    else:
        form = JobForm()
    return render(request, 'input_form.html', {'form': form})


def output_values(request):  # Test function to output all objects from the database
    len(values)
    return render(request, 'output.html', {'values': values})


def filter(request, type):
    return render(request, 'index_filter.html', {
        'postings': values,
        "typefiltered":type
    })



