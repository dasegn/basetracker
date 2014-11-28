from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from bt.models.services import Service

# Create your views here.
#@login_required
def index(request):
	template = loader.get_template('services.html')
	try:
		services = Service.objects.all()
	except Service.DoesNotExist:
		services = None

	context = RequestContext(request, {
		'services': services,
	})
	return HttpResponse(template.render(context))
