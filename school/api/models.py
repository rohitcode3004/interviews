from django.db import models

# Create your models here.

class Class(models.Model):
	cl_name = models.CharField(max_length=50)
	no_of_student = models.IntegerField(blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.cl_name

class Subject(models.Model):
	sub_name = models.CharField(max_length=200)
	sub_class = models.ForeignKey(Class, null=True, on_delete=models.SET_NULL)  # on delete this subject will remain in the db with null values as class subject
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.sub_name


class Student(models.Model):
	st_name = models.CharField(max_length=200)
	st_address = models.TextField(blank=True)
	st_class = models.ForeignKey(Class, null=True, on_delete=models.SET_NULL)
	st_subject =  models.ManyToManyField(Subject)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.st_name
