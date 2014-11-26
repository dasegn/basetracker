#-*- coding: utf-8 -*-


class CurrentUsr(object):
	def __init__(self, usr):
		self.full_name = self.nice_name(usr)
		self.avatar = usr.profile.get_avatar_url()

	def nice_name(self, user):
		return user.get_full_name() or user.username
