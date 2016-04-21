from django.db import models

from clients.models import Client

# Create your models here.
class Office(models.Model):
	name = models.CharField(max_length=100, default=None)
	currency = models.CharField(max_length=3, default=None)

	def __str__(self):
		return self.name

	# Custom method used to return the clients on a given office
	def clientsList(self):
		x = Client.objects.filter(office=self.id)
		return x