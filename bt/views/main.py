from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
	template = loader.get_template('main.html')
	context = Context({
		'fullName': nice_name(request.user),
		'avatar': request.user.profile.get_avatar_url(),
	})
	return HttpResponse(template.render(context))

def nice_name(user):
	return user.get_full_name() or user.username