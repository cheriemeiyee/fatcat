from django import forms

from .models import Employee

class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=300)
    job = forms.CharField(max_length=300)
    department = forms.CharField(max_length=300)