#-*- coding: utf-8 -*-

class CurrentUsr(object):
	def __init__(self, usr):
		if usr.is_authenticated():
			self.full_name = self.nice_name(usr)
			self.id = usr.pk
			self.avatar = usr.profile.get_avatar_url()

	def nice_name(self, user):
		return user.get_full_name() or user.username


def get_dashboard_data(request):
	context = {}
	context['cuser'] = CurrentUsr(request.user)
	return context

