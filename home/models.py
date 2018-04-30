from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=300)
    job = models.CharField(max_length=300)
    department = models.CharField(max_length=300)
    salary = models.CharField(max_length=300)
    salary2 = models.CharField(max_length=300)


    def __str__(self):
        return self.name
