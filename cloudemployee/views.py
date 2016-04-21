from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	template = 'home.html'
	context_dict = {}
	return render(request, template, context_dict)
	# return HttpResponse("HomePage")