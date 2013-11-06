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





