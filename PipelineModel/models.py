from django.db import models

# Create your models here.
class Feature(models.Model):
	name = models.CharField(max_length=200)
	other = models.CharField(max_length=200)

class Parameter(models.Model):
	name = models.CharField(max_length=200)
	display_name = models.CharField(max_length=200)
	forms = models.CharField(max_length=200)
	value = models.TextField()

class Template(models.Model):
	name = models.CharField(max_length=200)

class Pipeline(models.Model):
	feature_id = models.ForeignKey(to='Feature')
	template_ip = models.ForeignKey(to='Template')

class TemplateParameter(models.Model):
	template_id = models.ForeignKey(to='Template')
	parameter_id = models.ForeignKey(to='Parameter')

class PipelineParameter(object):
	pipeline_id = models.ForeignKey(to='Pipeline')
	template_parameter_id = models.ForeignKey(to='TemplateParameter')
	value = models.TextField()