# -*- coding: utf-8 -*-

from bt.models.projects import Project, Comment
from bt.serializers.projects import ProjectSerializer, CommentSerializer

from rest_framework import viewsets

class ProjectViewSet(viewsets.ModelViewSet):
	def get_queryset(self):
		return Project.objects.all()

	serializer_class = ProjectSerializer
	queryset = Project.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
	serializer_class = CommentSerializer
	queryset = Comment.objects.all()

