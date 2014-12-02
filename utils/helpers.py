#-*- coding: utf-8 -*-

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
	context['bt_week'] = GetActiveWeek(request)

	return context

class GetActiveWeek(object):
	def __init__(self,request):
		year = request.GET.get('year', None)
		week = request.GET.get('week', None)		
		date_pattern = '%d-%m-%Y'

		if year is None and week is None:
			self.week_now = datetime.now()
		else:
			self.week_now = self.get_first_day(int(year), int(week))

		self.week_last = (self.week_now - timedelta(days=7)).strftime(date_pattern)	
		self.week_next = (self.week_now + timedelta(days=7)).strftime(date_pattern)
		self.week_now = self.week_now.strftime(date_pattern)

	def get_week_range(self, week_date):
		year, week, dow = week_date.isocalendar()
		if dow == 1:
			start_date = week_date
		else:
			start_date = week_date - timedelta(dow)
		end_date = start_date + timedelta(6)
		return (start_date, end_date)

	def get_first_day(self, year, weeknum):
		ret = datetime.strptime('%04d-%02d-1' % (year, weeknum), '%Y-%W-%w')
		if date(year, 1, 4).isoweekday() > 4:
			ret -= timedelta(days=7)
		return ret