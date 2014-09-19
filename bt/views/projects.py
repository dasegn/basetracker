from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
	template = loader.get_template('admin/projects/index.html')
	context = Context({
		'variable': 'desde vista',
	})
	return HttpResponse(template.render(context))

def detail(request, project_id):
    return render_to_response(
    	'admin/projects/index.html',
    	{ 'project_id' : project_id },
    	RequestContext(request, {}),
    )