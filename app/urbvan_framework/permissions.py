# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.permissions import BasePermission


class IsAnonymousUser(BasePermission):
    """ Allows only read access to the users """
    def has_permission(self, request, view):
        return request.user.is_anonymous or \
               request.user.is_superuser or request.user.is_staff


class IsAdminUser(BasePermission):
    """ Allows access only to admin users. """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsSuperUser(BasePermission):
    """ Allows access only to superusers. """
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
