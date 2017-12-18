from django.db import models

# Create your models here.
class  Feature(models.Model):
	name = models.CharField(max_length=200)
	other = models.CharField(max_length=200)

class  Parameter(models.Model):
	name = models.CharField(max_length=200)
	display_name = models.CharField(max_length=200)
	forms = models.CharField(max_length=200)
	value = models.TextField()

class Template(models.Model):
	name = models.CharField(max_length=200)
	parameter_list = 
		