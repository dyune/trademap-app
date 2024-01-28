from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from trademap.forms import AccountForm
from .models import Account
from .forms import AccountForm
# Create your views here.

# home page accessed


def index(request):
    return render(request, 'index.html')

# home page -> make a post


def make_post(request):
    return HttpResponse('make a post')

# home page -> slug


def post_details(request):
    return HttpResponse('more details')


def input_form(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('output_values')  # Redirect to output view
    else:
        form = AccountForm()
    return render(request, 'input_form.html', {'form': form})


def output_values(request):
    values = Account.objects.all()  # Fetch all objects from the database
    return render(request, 'output.html', {'values': values})
