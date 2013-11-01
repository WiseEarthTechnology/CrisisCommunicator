"""
Filename: resources/urls.py
Authors:Seshagiri Prabhu
Copyright: Wise Earth Technology
Credits:Bithin Alangot
license:PeaceOSL
This file is part of the CrisisCommunicator Project.  
It is licensed under the Peaceful Open Source License.  
Please see the license terms in PeaceOSL.txt
"""
from django.conf.urls.defaults import *

from views import resource, delete_resource

urlpatterns = patterns('',
        (r'^/$', resource),
        (r'^/add/$',resource),
        (R'^/delete/$', delete_resource),
)
