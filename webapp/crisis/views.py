"""
Filename : crisis/views.py
Authors : Seshagiri Prabhu 
Copyright : Wise Earth Technology 
Credits : Bithin Alangot
This file is a part of the CrisisCommunicator Project...
It is licenced under the Peaceful Open Source License...
Please see the license terms in the PeaceOSL.txt
-
Redistribution and use of the software accompanying this license in source and 
binary forms, with or without modification, are permitted provided that the 
following conditions are met:

    1. Redistributions of source code must retain the above copyright notice, 
	this list of conditions and the following disclaimer.
    2. Redistributions in binary form must reproduce the above copyright 
	notice, this list of conditions and the following disclaimer in the 
	documentation and/or other materials provided with the distribution.
    3. Modifications to the source code must retain the above copyright 
	notice, this list of conditions, and the following disclaimer, and may 
	not include further conditions or licensing which go against the spirit 
	of this license.
    4. This software may not be used to cause deliberate harm to any 
	individual, either directly or indirectly, in any form.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER, AUTHORS, OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE 
GOODS OR SERVICES; LOSS OF USE, DATA, MONEY, POSSESSIONS, OR LIFE; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY 
OF SUCH DAMAGE.
"""
# Create your views here
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from random import randint

from refugeecenter.models import RefugeeCenter
from assessment.models import Emergency, Crime, RoadAssessment
from resources.models import Resource
from crisis.models import TrackCommunicator, Global
from crisis.helper import generate_gid

"""
The main page where the map will be shown.

The main page will contain map and feed. 

User can click on the map to enter the details. 

"""


def home(request):

    """
    View to render map with all the details marked on it. The main page also 
    contain message feeds, mostly listing message from the ARPS queue.

    """

    if request.session['loggedInside'] == True:
        #Have to retrieve all the details to be shown on to the map and feed
        refugee_center = RefugeeCenter.objects.all()
        emergency = Emergency.objects.all()
        crime = Crime.objects.all()
        road = RoadAssessment.objects.all()
        resource = Resource.objects.all()
        return render_to_response('crisis/home.html', {'refugee_center':refugee_center, 'emergency':emergency,\
                                    'crime':crime, 'road':road, 'resources': resource},RequestContext(request))
    else:
        return HttpResponseRedirect('/')





