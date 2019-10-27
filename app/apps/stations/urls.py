# coding: utf8
from django.urls import path
from .v1 import views as views_v1

urlpatterns_v1_locations = ([

    path('',
         views_v1.LocationView.as_view(),
         name='v1_list_create_location'),

], 'locations')

urls_v1_stations = ([
    path(
        'stations/',
        views_v1.StationModelListView.as_view(),
        name="stations-list"
    ),
    path(
        'stations/<str:pk>/',
        views_v1.StationModelDetailView.as_view(),
        name="stations-detail"
    ),
    path(
        'stations/create',
        views_v1.StationModelCreateView.as_view(),
        name="stations-create"
    ),
    path(
        'stations/delete/<str:pk>',
        views_v1.StationModelDeleteView.as_view(),
        name="stations-delete"
    ),
], 'stations')
