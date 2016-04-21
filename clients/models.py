from django.db import models

# Create your models here.
class Client(models.Model):
	# 'offices.Office' is used to avoid conflict of importing models with Office
	office = models.ForeignKey('offices.Office')
	name = models.CharField(max_length=100, default=None)

	def __str__(self):
		return self.name

	# Custom method used to return contact persons on a client
	def contactList(self):
		x = Contact.objects.filter(client=self.id)
		return x

class Contact(models.Model):
	client = models.ForeignKey(Client)
	last_name = models.TextField()
	first_name = models.TextField(null=True, blank=True)
	email = models.EmailField(null=True, blank=True)

	def fullname(self):
		first_name = self.first_name
		last_name = self.last_name
		return "%s %s" % (first_name, last_name)

	def __str__(self):
		return self.fullname()