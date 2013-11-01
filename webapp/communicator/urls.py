"""
Filename: communicator/urls.py
Authors: Seshagiri Prabhu 
Copyright: Wise Earth Technology
Credits : Bithin Alangot
This file is part of the CrisisCommunicator Project.  
It is licensed under the Peaceful Open Source License.  
Please see the license terms in PeaceOSL.txt
"""
from django.conf.urls.defaults import *
from communicator.views import user_home, user_register, logout

urlpatterns = patterns('',
    (r'^$', user_home),
    (r'^crisis', include('crisis.urls')),
    (r'^assessment', include('assessment.urls')), 
    (r'^person', include('person.urls')),
    (r'^refugeecenter', include('refugeecenter.urls')),
    (r'^resource', include('resources.urls')),
    (r'^search/', include('haystack.urls')),
    (r'^register/$', user_register),
    (r'^logout/$', logout),
)
