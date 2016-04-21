from django.shortcuts import render

from . models import *

# Create your views here.
def index(request):
	template = 'clients/ListView.html'
	items = Client.objects.filter()
	context_dict = {}
	context_dict['items'] = items
	return render(request, template, context_dict)

def item(request, id):
	template = 'clients/DetailView.html'
	item = Client.objects.get(id=id)
	context_dict = {}
	context_dict['item'] = item
	return render(request, template, context_dict)

def contactItem(request, id):
	template = 'contacts/ContactDetailView.html'
	item = Contact.objects.get(id=id)
	context_dict = {}
	context_dict['item'] = item
	return render(request, template, context_dict)