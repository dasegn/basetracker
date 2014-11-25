# -*- coding: utf-8 -*-

from bt.viewsets.users import UserViewSet
from bt.viewsets.projects import ProjectViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'users', UserViewSet, base_name="users")
router.register(r'projects', ProjectViewSet, base_name="projects")
router.register(r'comments', CommentViewSet, base_name="comments")

