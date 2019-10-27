# coding: utf8
from rest_framework import serializers

from ..models import LocationModel, StationModel


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocationModel
        exclude = ('id', )


class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = StationModel
        exclude = ('id', )
