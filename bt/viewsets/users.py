# -*- coding: utf-8 -*-

from django.contrib.auth.models import User 
from bt.serializers.users import UserSerializer

from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
	def get_queryset(self):
		return User.objects.all()

	serializer_class = UserSerializer
	queryset = User.objects.all()
