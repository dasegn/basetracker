from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from bt.models.projects import Project
from utils.helpers import GetActiveWeek

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
	template = 'projects.html'
	try:
		project = Project.objects.get(pk=project_id)
	except Project.DoesNotExist:
		raise Http404

	week = GetActiveWeek(request)

	week_start = week.week_now[0].strftime(week.date_pattern)
	week_end = week.week_now[1].strftime(week.date_pattern)

	tasklists = project.tasklist_set.filter(
		list_start = week_start, 
		list_end = week_end
		).order_by('name')

	context = {
		'project_id' : project_id,
		'project' : project,
		'start' : week_start,
		'end' : week_end,
		'dates' : week.week_now[3],
		'tasklists' : tasklists
	}
	return render_to_response(template, context, context_instance=RequestContext(request))	
