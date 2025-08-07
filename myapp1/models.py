from django.db import models
class Employee(models.Model):
    firstname=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    job_title=models.CharField(max_length=200)# Create your models here.
    employee_id=models.PositiveIntegerField()
    
    def __str__(self):
        return self.firstname