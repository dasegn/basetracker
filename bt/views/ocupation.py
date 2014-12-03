from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
#@login_required
def index(request):
	template = loader.get_template('ocupation.html')
	try:
		users = User.objects.all()
	except User.DoesNotExist:
		users = None

	context = RequestContext(request, {
		'all_users': users,
	})
	return HttpResponse(template.render(context))