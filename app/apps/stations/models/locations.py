# coding: utf8
from django.db import models

from ...utils import create_id


class LocationModel(models.Model):
    """ Location object is the representation of physical station

        Fields:
            id -- This is the unique identifier for object instance.
            name -- This is the common identifier for a physical location.
            coordinates --  Latitude and Longuitude as string.
                            example. "19.4094937,-99.1634261"
            geometry -- Similar to coordinate but using with postgis
    """

    id = models.CharField(default=create_id('loc_'), primary_key=True,
                          max_length=30, unique=True)
    name = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=100, default="")
    # geometry = models.GeometryField() TODO install postgis to add this field

    def __str__(self):
        return self.name
