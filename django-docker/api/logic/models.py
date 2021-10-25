from django.db import models

# Create your models here.
class Agent(models.Model):
	genome = models.TextField(null=True)
