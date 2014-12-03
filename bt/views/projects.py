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
		projects = Project.objects.exclude(status__label='Cerrado')
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

	list_start = request.session["bt_week_date_start"]
	list_end = request.session["bt_week_date_end"]

	tasklists = project.tasklist_set.all().order_by('name')

	context = RequestContext(request, {
		'project_id' : project_id,
		'project' : project,
		'demo' : list_start + ' - ' + list_end,
		'dates' : request.session["bt_week_date"],
		'tasklists' : tasklists
	})	
	return HttpResponse(template.render(context))