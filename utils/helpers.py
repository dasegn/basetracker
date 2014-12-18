#-*- coding: utf-8 -*-
from datetime import date, datetime, timedelta
from django.contrib.auth.models import Group

class CurrentUsr(object):
	def __init__(self, usr):
		if usr.is_authenticated():
			self.full_name = self.nice_name(usr)
			self.id = usr.pk
			self.avatar = usr.profile.get_avatar_url()

	def nice_name(self, user):
		return user.get_full_name() or user.username

class CurrentGroup(object):
	def __init__(self, request):
		self.groups = Group.objects.all().order_by('team__order')
		req_group = request.GET.get('group', None)

		if req_group is None:
			if 'bt_group' in request.session.keys():
				req_group = request.session["bt_group"]
			else:
				req_group = 'all'

		self.group = req_group
		self.group_name = self.get_group_name()
		self.group_url = self.get_group_url(request)

		request.session["bt_group"] =  self.group
		request.session.modified = True		

	def get_group_name(self):
		try:
			self.group = int(self.group)
			return Group.objects.get(id=self.group).name
		except(ValueError):
			return 'Todos'			

	def get_group_url(self, request):
		if len(request.GET) > 0:
			if 'group' in request.GET.keys():
				req = request.GET.copy()
				req.pop('group')
				return '?%s' % (req.urlencode())
			else:
				return '?%s' % (request.GET.urlencode())
		else:
			return '?'

def get_dashboard_data(request):	
	context = {}
	context['cuser'] = CurrentUsr(request.user)
	context['cgroup'] = CurrentGroup(request)
	context['current_url'] = request.path
	context['current_url_full'] = request.get_full_path()
	context['bt_week'] = GetActiveWeek(request)
	context['bt_param_sep'] = params_separator(request)
	return context

class GetActiveWeek(object):
	def __init__(self,request):
		year = request.GET.get('year', None)
		week = request.GET.get('week', None)		
		self.date_pattern = '%Y-%m-%d'

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
		self.week_default = self.get_week_range(datetime.now())

		request.session["bt_week_date"] =  '%d/%d' % (self.week_now[2] , self.week_now[3])
		request.session["bt_week_date_start"] =  self.week_now[0].strftime(self.date_pattern)	
		request.session["bt_week_date_end"] =  self.week_now[1].strftime(self.date_pattern)	
		request.session.modified = True

	def get_week_range(self, week_date):
		year, week, dow = week_date.isocalendar()
		if dow == 1:
			start_date = week_date
		else:
			start_date = self.get_first_day(year,week)
		end_date = start_date + timedelta(6)
		return (start_date, end_date, year, week)

	def get_first_day(self, year, weeknum):
		try:
			ret = datetime.strptime('%04d-%02d-1' % (year, weeknum), '%Y-%W-%w')
		except(ValueError):
			ret = datetime.now()
		if date(year, 1, 4).isoweekday() > 4:
			ret -= timedelta(days=7)
		return ret

def params_separator(request):
	if request.method == 'GET':
		return '?' if (len(request.GET.items()) == 0 ) else '&'
	else:
		return 'none'