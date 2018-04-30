from django.http import HttpResponse
from django.shortcuts import render, redirect
from functools import wraps
import json
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from . import placeid



# def index(request):
# 	return render(request, 'home.html')


def index(request):
    employee_list = Employee.objects.all()
    paginator = Paginator(employee_list, 52)  # Show 52 employees per page

    page = request.GET.get('page')
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        hotels = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        hotels = paginator.page(paginator.num_pages)

    context = {
        'employees': employees,
    }
    return render(request, 'searchresults.html', context)

