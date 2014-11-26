from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from utils.helpers import CurrentUsr

# Create your views here.
#@login_required
#def index(request):
#	template = loader.get_template('admin/projects/index.html')
#	context = Context({
#		'variable': 'desde vista',
#	})
#	return HttpResponse(template.render(context))

def detail(request, project_id):
	template = loader.get_template('projects.html')
	context = Context({
		'cuser': CurrentUsr(request.user),
		'project_id' : project_id,
	})	
	return HttpResponse(template.render(context))