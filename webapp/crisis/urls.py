"""
Filename: crisis/urls.py
Authors: Bithin Alangot Seshagiri Prabhu Harish Navnit
Copyright: Wise Earth Technology
This file is part of the CrisisCommunicator Project.  
It is licensed under the Peaceful Open Source License.  
Please see the license terms in PeaceOSL.txt
"""
from django.conf.urls.defaults import *

from views import home

urlpatterns = patterns('',
        (r'^/$', home),
)
