"""
Filename: refugeecenter/views.py
Authors: Bithin Alangot Seshagiri Prabhu Harish Navnit
Copyright: Wise Earth Technology
This file is part of the CrisisCommunicator Project.  
It is licensed under the Peaceful Open Source License.  
Please see the license terms in PeaceOSL.txt
"""
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from random import randint

from forms import RefugeeCenterForm, RefugeeCenterUpdateForm
from models import RefugeeCenter
from crisis.helper import generate_gid
from crisis.forms import CommentForm

import simplejson as json
from haystack.query import *

def refugee_center(request):

    """
    View to enter a new refugee center details into the crisis communicator. 

    """

    if request.method == 'POST':
        refugee_center_form = RefugeeCenterForm(request.POST)
        valid_refugee_center_form = refugee_center_form.is_valid()
        #gid need to be generated
                # Have to get ack from all the crisis communicator to make response_status true. 
        if valid_refugee_center_form: 
            refugee_center_form_data = refugee_center_form.save(commit=False)
            refugee_center_form_data.gid = generate_gid()           
            refugee_center_form_data.save() 
            return HttpResponseRedirect('/crisis/')
        else:
            return render_to_response('refugeecenter/refugeecenter.html', {'refugeecenter_form':
                refugee_center_form}, RequestContext(request))
    else:
        initial = {}
        if request.GET.get('q') is not None:
            lnglat = request.GET.get('q').split(",")
            initial = {
                'latitude':float(lnglat[0]),
                'longitude':float(lnglat[1]),
            }

        return render_to_response('refugeecenter/refugeecenter.html', {'refugeecenter_form':
            RefugeeCenterForm(initial)}, RequestContext(request))


        

def refugee_center_update(request, center_id):
    """
    View to update a refugee center details.

    """
    c_details = get_object_or_404(RefugeeCenter, center_id=center_id)
    initial = {
        'center_id':c_details.center_id, 'place':c_details.place, 'latitude':c_details.latitude,\
        'longitude':c_details.longitude, 'population':c_details.population, 'population_capacity'\
        :c_details.population_capacity, 'supplies_available_for':c_details.supplies_available_for
    }

    if request.method == 'POST':
        refugee_center_form = RefugeeCenterUpdateForm(request.POST)
        valid_refugee_center_form = refugee_center_form.is_valid()

        if valid_refugee_center_form:
            form_details = refugee_center_form.save(commit=False)
            update_refugee_center = RefugeeCenter.objects.get(center_id=center_id)
            update_refugee_center.center_id = c_details.center_id
            update_refugee_center.place = form_details.place 
            update_refugee_center.latitude = form_details.latitude
            update_refugee_center.longitude = form_details.longitude
            update_refugee_center.population = form_details.population
            update_refugee_center.population_capacity = form_details.population_capacity
            update_refugee_center.supplies_available_for = form_details.supplies_available_for
            update_refugee_center.save()
            return HttpResponseRedirect('/crisis/')
        else:
            return render_to_response('refugeecenter/refugeecenter_update.html',{'refugeecenter_form': \
                    RefugeeCenterUpdateForm(initial)}, RequestContext(request))
    else:
        return render_to_response('refugeecenter/refugeecenter_update.html',{'refugeecenter_form': \
                RefugeeCenterUpdateForm(initial)}, RequestContext(request))


def refugee_center_list(request):
    """
    View to list all the refugee center registered with the crisis communicator.

    """

    refugee_center_details = RefugeeCenter.objects.all()
    paginator = Paginator(refugee_center_details, 2)

    page = request.GET.get('page')
    try:
        refugeecenter = paginator.page(page)
    except PageNotAnInteger:
        refugeecenter = paginator.page(1)
    except EmptyPage:
        refugeecenter = paginator.page(paginator.num_pages)

    return render_to_response('refugeecenter/refugeecenter_list.html', {'refugeecenter':\
            refugeecenter}, RequestContext(request))



def autocomplete(request):
    search_results = SearchQuerySet().autocomplete(center_id__startswith=request.GET.get('q',''))[:5]
    suggestions = [result.center_id for result in search_results]

    the_data = json.dumps({
            'results':suggestions
        })
    return HttpResponse(the_data, content_type='application/json')




def search_refugeecenter(request):

    if request.method == 'POST':
        try:
            term = str(request.POST['q'])
        except:
            return render_to_response('search/search_center.html', {}, RequestContext(request))

        results = SearchQuerySet().auto_query(term)
        names = []
        for r in results:
            names.append(r.object)

        return render_to_response('search/search_center.html', {'result': names}, RequestContext(request))
    else:
        return render_to_response('search/search_center.html', {}, RequestContext(request))


def delete_refugeecenter(request):

    if request.method == 'GET':
        try:
            center_id = RefugeeCenter.objects.get(pk=str(request.GET['q']))
            center_id.delete()
            return HttpResponseRedirect('/crisis/')
        except:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/crisis/')


