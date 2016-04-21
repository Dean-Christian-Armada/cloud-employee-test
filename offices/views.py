from django.shortcuts import render

from . models import *

# Create your views here.
def index(request):
	template = 'offices/ListView.html'
	items = Office.objects.filter()
	context_dict = {}
	context_dict['items'] = items
	return render(request, template, context_dict)

def item(request, id):
	template = 'offices/DetailView.html'
	item = Office.objects.get(id=id)
	context_dict = {}
	context_dict['item'] = item
	return render(request, template, context_dict)