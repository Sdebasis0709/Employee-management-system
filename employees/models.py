# employees/models.py

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    employee_id = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    join_date = models.DateField()

    def __str__(self):
        return self.name
