from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from crisis.models import User, Comment
from assessment.models import Crime, RoadAssessment, Emergency

from forms import EmergencyForm, CrimeForm, RoadAssessmentForm, CrimeUpdateForm
from crisis.forms import CommentForm
from crisis.helper import generate_gid

from random import randint

def emergency(request):

    """
    View to report emergency situtation that occurs during a disaster. 

    """

    if request.method == 'POST':
        emergency_form = EmergencyForm(request.POST)
        comment_form = CommentForm(request.POST)
        valid_emergency_form = emergency_form.is_valid()
        valid_comment_form = comment_form.is_valid()
        if valid_emergency_form and valid_comment_form:
            comment_form_data = comment_form.save(commit=False)
            _comment_id = randint(1,1000)
            comment_form_data.comment_id = _comment_id
            comment_form_data.user_id = get_object_or_404(User, user_id=request.session['user_id'])
            comment_form_data.save()
            emergency_form_data = emergency_form.save(commit=False)
            emergency_form_data.gid = generate_gid()
            emergency_form_data.comment = get_object_or_404(Comment, comment_id=_comment_id)
            emergency_form_data.save()
            return HttpResponseRedirect('/crisis/')
        else:
            return render_to_response('assessment/emergency.html',{'emergency_form':emergency_form,\
                    'comment_form':comment_form}, RequestContext(request))
    else:
        initial = {}
        if request.GET.get('q') is not None:
            lnglat = request.GET.get('q').split(",")
            initial = {
                'latitude':float(lnglat[0]),
                'longitude':float(lnglat[1]),
            }

        return render_to_response('assessment/emergency.html', {'emergency_form':EmergencyForm(initial),\
                'comment_form':CommentForm()}, RequestContext(request))


def emergency_delete(request):

    if request.method == 'GET':
        try:
            emergency_id = Emergency.objects.get(pk=str(request.GET['q']))
            emergency_id.delete()
            return HttpResponseRedirect('/crisis/')
        except:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/crisis/')
        
def crime(request):

    """
    View to report crime in a disaster area. 

    """

    if request.method == 'POST':
        crime_form = CrimeForm(request.POST)
        comment_form = CommentForm(request.POST)    
        valid_crime_form = crime_form.is_valid()
        valid_comment_form = comment_form.is_valid()

        if valid_comment_form and valid_crime_form:
            comment_form_data = comment_form.save(commit=False)
            _comment_id = randint(1,1000) # should we replace with some other assignment
            comment_form_data.comment_id = _comment_id
            comment_form_data.user_id = get_object_or_404(User, user_id=request.session['user_id'])
            comment_form_data.save()
            crime_form_data = crime_form.save(commit=False)
            crime_form_data.gid = generate_gid()
            crime_form_data.comment = get_object_or_404(Comment, comment_id=_comment_id)
            crime_form_data.save()
            return HttpResponseRedirect('/crisis/')
        else:
            return render_to_response('assessment/crime.html', {'crime_form':crime_form,\
                    'comment_form':comment_form},RequestContext(request))

    else:
        initial = {}
        if request.GET.get('q') is not None:
            lnglat = request.GET.get('q').split(",")
            initial = {
                'latitude':float(lnglat[0]) ,
                'longitude':float(lnglat[1]),
            }
        return render_to_response('assessment/crime.html', {'crime_form':CrimeForm(initial),\
                'comment_form':CommentForm()},RequestContext(request))

def crime_delete(request):

    if request.method == 'GET':
        try:
            crime_id = Crime.objects.get(pk=str(request.GET['q']))
            crime_id.delete()
            return HttpResponseRedirect('/crisis/')
        except:
            return HttpResponseRedirect('')
    else:
        return HttpResponseRedirect('/')

        
def crime_update(request, latitude, longitude):
    crime_details = get_object_or_404(Crime, latitude = latitude ,longitude = longitude)
    init_crime = { 'latitude' : crime_details.latitude , 'longitude' : crime_details.longitude, \
            'crime_type' : crime_details.crime_type, 'criminals' : crime_details.criminals
            }
    if request.method == 'POST':
        crime_update_form =  CrimeUpdateForm(request.POST)
        valid_crime_update_form = crime_update_form.is_valid()

        if valid_crime_update_form:
            crime_form_details = crime_update_form.save(commit = False)
            update_c = Crime.objects.get(latitude = latitude, longitude = longitude)
            update_c.latitude = crime_form_details.latitude
            update_c.longitude = crime_form_details.longitude
            update_c.crime_type = crime_form_details.crime_type
            update_c.criminals = crime_form_details.criminals

            update_c.save()
            return HttpResponseRedirect('/crisis/')
        else:
            return render_to_response('assessment/crime_update.html', { 'crime_form' : CrimeUpdateForm(init_crime)}\
                    , RequestContext(request))

    else:
        return render_to_response('assessment/crime_update.html', { 'crime_form' : CrimeUpdateForm(init_crime)}\
                , RequestContext(request))


            


def road_assessment(request):

    """
    View to read the condition of a road or path in a disaster zone.

    """

    if request.method == 'POST':
        road_form = RoadAssessmentForm(request.POST)
        comment_form = CommentForm(request.POST)
        valid_road_form = road_form.is_valid()
        valid_comment_form = comment_form.is_valid()

        if valid_road_form and valid_comment_form:
            comment_form_data = comment_form.save(commit=False)
            _comment_id = randint(1,1000)
            comment_form_data.comment_id = _comment_id
            comment_form_data.user_id = get_object_or_404(User, user_id=request.session['user_id'])
            comment_form_data.save()
            road_form_data = road_form.save(commit=False)
            road_form_data.gid = generate_gid()
            road_form_data.comment = get_object_or_404(Comment, comment_id=_comment_id)
            road_form_data.save()
            return HttpResponseRedirect('/crisis/')
        else:
            return render_to_response('assessment/road.html', {'road_form':RoadAssessmentForm(), \
                    'comment_form':CommentForm()},RequestContext(request))
    else:
        initial = {}
        if request.GET.get('q') is not None:
            lnglat = request.GET.get('q').split(",")
            initial = {
                'latitude':float(lnglat[0]) ,
                'longitude':float(lnglat[1]),
            }

        return render_to_response('assessment/road.html', {'road_form':RoadAssessmentForm(initial), \
                'comment_form':CommentForm()}, RequestContext(request))


def road_assessment_update(request, latitude, longitude):
    road_details = get_object_or_404(RoadAssessment, latitude = latitude ,longitude = longitude)
    init_road = { 'latitude' : road_details.latitude , 'longitude' : road_details.longitude, \
            'assessment' : road_details.assessment }
    if request.method == 'POST':
        road_update_form =  RoadAssessmentForm(request.POST)
        valid_road_update_form = road_update_form.is_valid()

        if valid_road_update_form:
            road_form_details = road_update_form.save(commit = False)
            update_r = RoadAssessment.objects.get(latitude = latitude, longitude = longitude)
            update_r.latitude = road_form_details.latitude
            update_r.longitude = road_form_details.longitude
            update_r.assessment = road_form_details.assessment

            update_r.save()
            return HttpResponseRedirect('/crisis/')
        else:
            return render_to_response('assessment/road_update.html', { 'road_form' : RoadAssessmentForm(init_road)}\
                    , RequestContext(request))

    else:
        return render_to_response('assessment/road_update.html', { 'road_form' : RoadAssessmentForm(init_road)}\
                , RequestContext(request))


def road_delete(request):

    if request.method == 'GET':
        try:
            road_data = RoadAssessment.objects.get(pk=str(request.GET['q']))
            road_data.delete()
            return HttpResponseRedirect('/crisis/')
        except:
            return HttpResponseRedirect('/')
    
    else 
         return HttpResponseRedirect('/crisis/')
       
def rendezvous(request):

    """
    View to set meetings between the response Personal to discuss disaster management strategy

    """

    return render_to_response('assessment/renezvous.html', {'rendezvous':RendezvousForm()}, \
            RequestResponse(request))
