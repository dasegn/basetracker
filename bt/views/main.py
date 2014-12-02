from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from utils.logentries import ListLogEntries

def index(request):
	template = loader.get_template('main.html')
	log_entries = ListLogEntries(9)	
	context = RequestContext(request, {
		'entries': log_entries,	
	})
	return HttpResponse(template.render(context))
