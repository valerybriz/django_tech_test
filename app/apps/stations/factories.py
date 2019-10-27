# coding: utf8
import factory
from .models import LocationModel, StationModel


class LocationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = LocationModel

    name = factory.Faker('slug')
    coordinates = f"{factory.Faker('latitude')},{factory.Faker('longitude')}"


class StationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = StationModel

    location = factory.SubFactory(LocationFactory)
    order = factory.Faker('random_int').generate({})
    is_active = True
