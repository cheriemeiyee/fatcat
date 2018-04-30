from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import json

from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render(request, 'index.html')


@login_required
def dashboard(request):
    user = request.user
    auth0user = user.social_auth.get(provider="auth0")
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture']
    }

    return render(request, 'dashboard.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })

def deptsearch(request):
    return render(request, 'deptsearch.html')

def results(request):
    employee_list = Employee.objects.all()
    paginator = Paginator(employee_list, 52)  # Show 52 employees per page

    page = request.GET.get('page')
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        employees = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        employees = paginator.page(paginator.num_pages)

    context = {
        'employees': employees,
    }
    return render(request, 'results.html', context)
