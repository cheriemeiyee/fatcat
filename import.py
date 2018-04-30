import sys, os, django


sys.path.append("/Users/nithyarajan/Cmpe172/fatcat/") #here store is root folder(means parent).

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fatcat.settings")
django.setup()

from home.models import Employee
import csv

with open('Employees.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # The header row values become your keys
        name = row['NAME'].strip()
        job = row['JOB TITLE'].strip()
        department = row['DEPARTMENT'].strip()
        salary = row['EMPLOYEE ANNUAL SALARY'].strip()
        salary2 = row['ESTIMATED ANNUAL SALARY MINUS FURLOUGHS'].strip()

        new_employee = Employee(name = name, job = job, department = department, salary = salary, salary2 = salary2)
        #print(new_employee.name)
        #print(new_employee.job)
        new_employee.save()
