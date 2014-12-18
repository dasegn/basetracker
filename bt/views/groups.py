from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
#@login_required
def index(request):
	template = loader.get_template('groups.html')
	try:
		groups = Group.objects.all().order_by('team__order')
	except Group.DoesNotExist:
		groups = None

	context = RequestContext(request, {
		'groups': groups,
	})
	return HttpResponse(template.render(context))
