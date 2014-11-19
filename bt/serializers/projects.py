# -*- coding: utf-8 -*-

from rest_framework import serializers

from bt.models.projects import Project, Comment

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = (
				'id', 
				'name',
				'description',
				'identifier',
				'parent',
				'access',
				'date_begin',
				'date_end',
				'date_created',
				'date_modified',
				'members',
				'type',
				'status',
				'kam',
				'admin',
				'rd',
				'client',
				'services',			
			)

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fileds = (
				'author',
				'project',
				'submit_date',
				'body',
			)