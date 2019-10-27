# coding: utf8
from urbvan_framework.views import (
    ListCreateView,
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from .schemas import LocationSchema, StationSchema
from .serializers import LocationSerializer, StationSerializer
from urbvan_framework.permissions import (
    IsAdminUser,
    IsAnonymousUser,
    IsSuperUser,
)
from ..models import LocationModel, StationModel


class LocationView(ListCreateView):
    permission_classes = (IsAnonymousUser,)
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer


"""
Station CRUD views
Permissions:
 - List view for all users
 - Retrive view for staff and superuser
 - Create and delete only for superuser
"""


class StationModelListView(ListAPIView):
    permission_classes = (IsAnonymousUser,)

    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer


class StationModelCreateView(CreateAPIView):
    permission_classes = (IsSuperUser,)

    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer


class StationModelDetailView(RetrieveAPIView):

    permission_classes = (IsAdminUser,)

    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer


class StationModelDeleteView(DestroyAPIView):

    permission_classes = (IsSuperUser, )

    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer
