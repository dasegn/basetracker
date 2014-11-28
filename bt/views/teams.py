from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
	template = loader.get_template('admin/profiles/index.html')
	context = RequestContext(request, {
		'variable': 'desde vista',
	})
	return HttpResponse(template.render(context))

def detail(request, profile_id):
	template = loader.get_template('admin/groups/index.html')
	context = RequestContext(request, {
		'profile_id': profile_id,
	})	
	return HttpResponse(template.render(context))
