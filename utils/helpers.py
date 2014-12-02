#-*- coding: utf-8 -*-
from importlib import import_module
from django.conf import settings
from datetime import date, datetime, timedelta

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
	context['current_url'] = request.path
	context['current_url_full'] = request.get_full_path()
	context['bt_week'] = GetActiveWeek(request)

	if 'bt_week_date' in request.session.keys():
		context['bt_week_select'] = 'Fecha: ' + request.session['bt_week_date']

	return context

class GetActiveWeek(object):
	def __init__(self,request):
		year = request.GET.get('year', None)
		week = request.GET.get('week', None)		
		self.date_pattern = '%d/%m/%y'

		if year is None and week is None:
			if 'bt_week_date' in request.session.keys():
				year, week = request.session["bt_week_date"].split("/")
				self.week_now = self.get_first_day(int(year), int(week))
			else:
				self.week_now = datetime.now()
		else:
			self.week_now = self.get_first_day(int(year), int(week))

		self.week_last_two = self.get_week_range(self.week_now - timedelta(days=14))
		self.week_last = self.get_week_range(self.week_now - timedelta(days=7))
		self.week_next = self.get_week_range(self.week_now + timedelta(days=7))
		self.week_next_two = self.get_week_range(self.week_now + timedelta(days=14))
		self.week_now = self.get_week_range(self.week_now)

		request.session["bt_week_date"] =  '%d/%d' % (self.week_now[2] , self.week_now[3])

	def get_week_range(self, week_date):
		year, week, dow = week_date.isocalendar()
		if dow == 1:
			start_date = week_date
		else:
			start_date = self.get_first_day(year,week)
		end_date = start_date + timedelta(6)

		start_date = start_date.strftime(self.date_pattern)	
		end_date = end_date.strftime(self.date_pattern)	
		return (start_date, end_date, year, week)

	def get_first_day(self, year, weeknum):
		ret = datetime.strptime('%04d-%02d-1' % (year, weeknum), '%Y-%W-%w')
		if date(year, 1, 4).isoweekday() > 4:
			ret -= timedelta(days=7)
		return ret
