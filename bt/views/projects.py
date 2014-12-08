from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required

# Controllers
from bt.models.projects import Project
from bt.models.services import Service
from bt.models.attributes import Attribute

# Helpers
from utils.helpers import GetActiveWeek

# Create your views here.
#@login_required
def index(request):
	template = loader.get_template('list_projects.html')
	try:
		projects = Project.objects.exclude(status__label='Cerrado')
	except Project.DoesNotExist:
		projects = None

	clients_count = Attribute.objects.filter(type='project-client').count()
	services_count = Service.objects.all().count()
	week = GetActiveWeek(request)

	class SkelProject: pass
	elements = []
	for project in projects:
		elem = SkelProject()
		elem.project = project
		elem.risks = project.get_risk_totals(
			year = week.week_now[2],
			week = week.week_now[3]
		)
		elements.append(elem)



	context = RequestContext(request, {
		'projects': projects,
		'clients_count': clients_count,
		'services_count': services_count,
		'elements': elements
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
		'tasklists' : tasklists,
		'project_totals' : project.get_risk_totals(
			year = week.week_now[2],
			week = week.week_now[3]
		)		
	}
	return render_to_response(template, context, context_instance=RequestContext(request))	
