# coding: utf8
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import RetrieveModelMixin, DestroyModelMixin

from .mixins import (CreateModelMixin, ListModelMixin)
from .schemas import PaginationResponse
from .authentication import CustomTokenAuthentication


class CreateAPIView(CreateModelMixin, GenericAPIView):
    """
    Concrete view for creating a model instance.
    """
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListAPIView(ListModelMixin, GenericAPIView):
    """
    Concrete view for listing a queryset.
    """

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    pagination_class = PaginationResponse

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ListCreateView(CreateAPIView, ListAPIView):
    """ Concrete view for listing a queryset or creating a model instance """
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class RetrieveAPIView(GenericAPIView, RetrieveModelMixin):
    """ Concrete view for listing a queryset or creating a model instance """
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class DestroyAPIView(GenericAPIView, DestroyModelMixin):
    """ Concrete view for listing a queryset or creating a model instance """
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

