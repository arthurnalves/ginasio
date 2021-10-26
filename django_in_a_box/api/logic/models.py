from django.db import models


class Agent(models.Model):
	genome = models.TextField(null=True)


class Environment(models.Model):
	name = models.CharField(max_length=100, null=True)
