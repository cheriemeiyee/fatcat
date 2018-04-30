from django.db import models

class Employee(models.Model):
	name = models.CharField(max_length=300)
	job = models.CharField(max_length=300)
	department = models.CharField(max_length=300)
	salary = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	salary2 = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)


	def __str__(self):
		return self.name