#-*- coding: utf-8 -*-

from django.contrib.admin.models import LogEntry

def ListLogEntries(how_many):
	last_actions = LogEntry.objects.all().order_by("-action_time")[:how_many]

	for entry in last_actions:
		entry.action_time = entry.action_time.strftime("%A %d de %B de %Y a las  %H:%M")
		entry.action_color = get_color(entry)
		entry.icon = get_icon(entry)
		entry.action_flag = verb(entry)
	return last_actions

def get_color(action):
	""" Return verb label for a given action code"""
	if action.is_deletion():
		return "danger"
	elif action.is_addition():
		return "success"
	elif action.is_change():
		return "info"

def get_icon(action):
	""" Return verb label for a given action code"""
	if action.is_deletion():
		return "fa-minus-square-o"
	elif action.is_addition():
		return "fa-plus-square-o"
	elif action.is_change():
		return "fa-pencil-square-o"

def verb(action):
	""" Return verb label for a given action code"""
	if action.is_deletion():
		return u"eliminó"
	elif action.is_addition():
		return u"agregó"
	elif action.is_change():
		return u"modificó"
