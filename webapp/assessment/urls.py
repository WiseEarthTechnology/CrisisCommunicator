"""
Filename: assessment/urls.py 
Authors: Seshagiri Prabhu 
Copyright: Wise Earth Technology
Credits : Bithin Alangot
This file is part of the CrisisCommunicator Project.  
It is licensed under the Peaceful Open Source License.  
Please see the license terms in PeaceOSL.txt
"""
from django.conf.urls.defaults import *

from views import road_assessment, emergency, crime, crime_update, road_assessment_update, \
                    road_delete, emergency_delete, crime_delete

urlpatterns = patterns('',
        (r'^/$', road_assessment),
        ('^/road/add/$', road_assessment),
        ('^/road/delete/$', road_delete),
        ('^/road/(?P<latitude>\w+)/(?P<longitude>\w+)/update$',road_assessment_update),
        ('^/emergency/add/$', emergency), 
        ('^/emergency/map/$', emergency),
        ('^/emergency/delete/$', emergency_delete), 
        ('^/crime/add/$', crime),
        ('^/crime/delete/$', crime_delete),
        ('^/crime/(?P<latitude>\w+)/(?P<longitude>\w+)/update$',crime_update),
)
