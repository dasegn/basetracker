#-*- coding: utf-8 -*-
from django.utils import formats
from django.contrib.admin.models import LogEntry

def ListLogEntries(how_many):
	last_actions = LogEntry.objects.all().order_by("-action_time")[:how_many]

	for entry in last_actions:
		entry.action_time = formats.date_format(entry.action_time, "DATETIME_FORMAT")
		if entry.is_deletion():
			entry.action_color = "danger"
			entry.icon = "fa-minus-square-o"
			entry.action_flag = u"eliminó"
		elif entry.is_addition():
			entry.action_color = "success"
			entry.icon = "fa-plus-square-o"
			entry.action_flag = u"agregó"
		elif entry.is_change():
			entry.action_color = "info"
			entry.icon = "fa-pencil-square-o"
			entry.action_flag = u"modificó"		

	return last_actions