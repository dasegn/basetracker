from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from bt.models.projects import Project

# Create your views here.
#@login_required
def index(request):
	template = loader.get_template('list_projects.html')
	try:
		projects = Project.objects.all()
	except Project.DoesNotExist:
		projects = None

	context = RequestContext(request, {
		'projects': projects,
	})
	return HttpResponse(template.render(context))

def detail(request, project_id):
	template = loader.get_template('projects.html')
	try:
		project = Project.objects.get(pk=project_id)
	except Project.DoesNotExist:
		raise Http404

	context = RequestContext(request, {
		'project_id' : project_id,
		'project' : project
	})	
	return HttpResponse(template.render(context))