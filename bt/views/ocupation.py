from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

# Helpers
from utils.helpers import GetActiveWeek, CurrentGroup

# Create your views here.
#@login_required
def index(request):
	template = loader.get_template('ocupation.html')
	cgroup = CurrentGroup(request)

	try:
		if(cgroup.group == 'all'):
			groups = Group.objects.all()
		else:
			groups = Group.objects.filter(id=int(cgroup.group))
	except Group.DoesNotExist:
		groups = None

	week = GetActiveWeek(request)

	class SkelGroup: pass
	elements = []
	for group in groups:
		elem = SkelGroup()
		elem.group = group
		elem.total = group.team.get_team_totals(
			year = week.week_now[2],
			week = week.week_now[3]
		)
		elements.append(elem)


	context = RequestContext(request, {
		'groups': elements,
	})
	return HttpResponse(template.render(context))