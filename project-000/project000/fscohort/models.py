from django.db import models
class Student(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	number = models.IntegerField()
# Create your models here.
