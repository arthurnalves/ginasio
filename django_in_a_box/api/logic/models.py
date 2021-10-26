from django.db import models
from django.contrib.postgres.fields import ArrayField

class Agent(models.Model):
	genome = models.TextField(null=True)

	
class Environment(models.Model):
	name = models.CharField(max_length=100, null=True)


class Data(models.Model):
	inputs = ArrayField(models.FloatField())
	ouputs = ArrayField(models.FloatField())
	environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
