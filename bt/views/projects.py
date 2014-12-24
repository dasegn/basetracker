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
def index(request, filter_type=None):
	template = loader.get_template('list_projects.html')
	week = GetActiveWeek(request)

	try:
		projects = Project.total.getweek(week.week_now[3], week.week_now[2])
	except Project.DoesNotExist:
		projects = None

	# Set Filter Type
	if filter_type:
		if filter_type == 'danger':
			projects = projects.danger()
		elif filter_type == 'warning':
			projects = projects.warning()
		elif filter_type == 'success':
			projects = projects.success()
			
	clients_count = Attribute.objects.filter(type='project-client').count()
	services_count = Service.objects.all().count()
	week = GetActiveWeek(request)

	context = RequestContext(request, {
		'projects': projects,
		'clients_count': clients_count,
		'services_count': services_count,
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

	tasklists = project.tsklst.filter(
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
