from django.db import models
from core import custom_fields

	
class Environment(models.Model):
	name = models.CharField(primary_key=True, max_length=100)


class Agent(models.Model):
	genome = models.TextField(null=True, blank=True)
	fitness = models.FloatField(null=True, blank=True)
	environment = models.ForeignKey(Environment, on_delete=models.CASCADE)

	def get_fitness(self):
		if not self.fitness:
			self.fitness = 10
			self.save()
		return self.fitness


class Data(models.Model):
	inputs = custom_fields.CommaSepField(null=True)
	outputs = custom_fields.CommaSepField(null=True)
	environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
