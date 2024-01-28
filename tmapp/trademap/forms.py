from django import forms
from .models import Account, JobPostings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'first_name', 'last_name', 'password', 'profession']

class JobForm(forms.ModelForm):
    class Meta:
        model = JobPostings
        fields = ['user', 'title', 'description', 'cost_offer', 'profession_type']





    