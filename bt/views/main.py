from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
	template = loader.get_template('main.html')
	context = Context({
		'variable': 'desde vista',
	})
	return HttpResponse(template.render(context))