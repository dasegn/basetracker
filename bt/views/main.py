from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from utils.logentries import ListLogEntries
from utils.helpers import CurrentUsr

def index(request):
	template = loader.get_template('main.html')
	log_entries = ListLogEntries(9)	
	context = Context({
		'cuser': CurrentUsr(request.user),
		'entries': log_entries,		
	})
	return HttpResponse(template.render(context))

def nice_name(user):
	return user.get_full_name() or user.username