"""
Filename: person/views.py
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
from haystack.query import *
import simplejson as json

from crisis.helper import generate_gid
from crisis.models import Comment, User
from crisis.forms import CommentForm

from models import Person, Refugee, Missing, Deceased
from forms import RefugeeForm, MissingForm, PersonForm, DeceasedForm, RefugeeUpdateForm, PersonUpdateForm, DeceasedUpdateForm

from random import randint

def refugee(request):

    """
    View to add a refugee to the crisis communicator db

    """

    if request.method == 'POST':
        person_form = PersonForm(request.POST)
        refugee_form = RefugeeForm(request.POST)
        valid_person_form = person_form.is_valid()
        valid_refugee_form = refugee_form.is_valid()

        if valid_person_form and valid_refugee_form:
            person_form.save()
            refugee_form_data = refugee_form.save(commit=False)
            refugee_form_data.gid = generate_gid()
            refugee_form_data.person_id = get_object_or_404(Person, person_id= \
                    person_form.cleaned_data['person_id'])
            refugee_form_data.save()
            return HttpResponseRedirect('/crisis/')
        else:
            return render_to_response('person/refugee.html', {'person_form':person_form,
                'refugee_form':refugee_form}, RequestContext(request))

    else:
        return render_to_response('person/refugee.html', {'person_form':PersonForm(),
            'refugee_form':RefugeeForm()}, RequestContext(request))


def refugee_update(request, person_id):
    person_details = get_object_or_404(Person, person_id = person_id)
    refugee_details = get_object_or_404(Refugee, person_id = person_id)
    init_person = {'person_id' : person_details.person_id, 'person_name' : person_details.person_name, \
            'gender' : person_details.gender, 'age' : person_details.age , 'hair_color' : person_details.hair_color,\
            'wounds' : person_details.wounds, 'height' : person_details.height, 'identification_mark' : \
            person_details.identification_mark, 'color_complexation' : person_details.color_complexation 
            }
    init_refugee = {'health_status' : refugee_details.health_status, 'center_id' : refugee_details.center_id
            }
    if request.method == 'POST':
        person_update_form = PersonUpdateForm(request.POST)
        refugee_update_form = RefugeeUpdateForm(request.POST)
        valid_person_update_form = person_update_form.is_valid()
        valid_refugee_update_form = refugee_update_form.is_valid()

        if valid_person_update_form and valid_refugee_update_form:
            person_form_details = person_update_form.save(commit = False)
            refugee_form_details = refugee_update_form.save(commit = False)
            update_p = Person.objects.get(person_id = person_id)
            update_r = Person.objects.get(person_id = person_id)

            update_p.person_name = person_form_details.person_name
            update_p.gender = person_form_details.gender
            update_p.age = person_form_details.age
            update_p.hair_color = person_form_details.hair_color
            update_p.wounds = person_form_details.wounds
            update_p.height = person_form_details.height
            update_p.identification_mark = person_form_details.identification_mark
            update_p.color_complaxation = person_form_details.color_complexation

            update_r.center_id = refugee_form_details.center_id
            update_r.health_status = refugee_form_details.health_status

            update_p.save()
            update_r.save()
            return HttpResponseRedirect('/crisis/')

        else:
            return render_to_response('person/refugee_update.html', {'refugee_form' : RefugeeUpdateForm(init_refugee),
                'person_form' : PersonUpdateForm(init_person)}, RequestContext(request))

    else:
        return render_to_response('person/refugee_update.html', {'refugee_form' : RefugeeUpdateForm(init_refugee),
            'person_form' : PersonUpdateForm(init_person)}, RequestContext(request))

    



#update will come here
def refugee_autocomplete(request):
    refugee_details = Refugee.objects.all()
    the_data=[]
    j=1;
    aaData ={}
    for i in refugee_details:
        aaData = {
            'person_name':i.person_id.person_name,
            'health_status':i.health_status,
            'gender':i.person_id.gender,
            'age':i.person_id.age,
            'DT_RowId': 'row_' + str(j),
            }
        the_data.append(aaData)
        j=j+1
       
    the_data = json.dumps({
        'sEcho': 1,
        'iTotalRecords': j-1,
        'iTotalDisplayRecords': j-1,
        'aaData':the_data
    })
    return HttpResponse(the_data, content_type='application/json')


def refugee_list(request):

    """
    View which will list all the refugees in the refugee center.

    """
    refugee_details = Refugee.objects.all()
    paginator = Paginator(refugee_details, 5)

    page = request.GET.get('page')
    try:
        refugee = paginator.page(page)
    except PageNotAnInteger:
        refugee = paginator.page(1)
    except EmptyPage:
        refugee = paginator.page(paginator.num_pages)

    return render_to_response('person/refugee_list.html', {'refugee':\
            refugee}, RequestContext(request))



def missing(request):

    """
    The view is to file missing person, in the diseaster area.

    """

    if request.method == 'POST':
        person_form = PersonForm(request.POST)
        missing_form = MissingForm(request.POST)
        comment_form = CommentForm(request.POST)
        valid_person_form = person_form.is_valid()
        valid_missing_form = missing_form.is_valid()
        valid_comment_form = comment_form.is_valid()
        if valid_person_form and valid_missing_form and valid_comment_form:
            person_form_data = person_form.save()
            missing_form_data = missing_form.save(commit=False)
            missing_form_data.gid = generate_gid()
            missing_form_data.person_id = get_object_or_404(Person, person_id= \
                    person_form_data.person_id)
            comment_form_data = comment_form.save(commit=False)
            _comment_id = randint(1,1000)
            comment_form_data.comment_id = _comment_id
            comment_form_data.user_id = get_object_or_404(User, user_id=request.session['user_id'])
            comment_form_data.save()
            missing_form_data.comment = get_object_or_404(Comment, comment_id=_comment_id)
            missing_form_data.save()
            return HttpResponseRedirect('/crisis/')
        else:
            return render_to_response('person/missing.html', {'person_form': person_form,\
                    'missing_form':missing_form, 'comment_form':\
                    comment_form, 'error':person_form, 'error1':missing_form, 'error2':comment_form},RequestContext(request))
    else:
        return render_to_response('person/missing.html', {'person_form': PersonForm(),\
                'missing_form':MissingForm(), 'comment_form': \
                CommentForm()}, RequestContext(request))



def missing_list(request):

    """
    View which will return all the missing person case entered into the \

    """
    missing_details = Missing.objects.all()
    paginator = Paginator(missing_details, 2)

    page = request.GET.get('page')
    try:
        missing = paginator.page(page)
    except PageNotAnInteger:
        missing = paginator.page(1)
    except EmptyPage:
        missing = paginator.page(paginator.num_pages)

    return render_to_response('person/missing_list.html', {'missing':\
            missing}, RequestContext(request))




def deceased(request):

    """
    View to add deceased people details. 

    """

    if request.method == 'POST':
        person_form = PersonForm(request.POST)
        deceased_form = DeceasedForm(request.POST)
        valid_person_form = person_form.is_valid()
        valid_deceased_form = deceased_form.is_valid()

        if valid_person_form and valid_deceased_form:
            person_form.save()
            deceased_form_data = deceased_form.save(commit=False)
            deceased_form_data.gid = generate_gid()
            deceased_form_data.person_id = get_object_or_404(Person, person_id= \
                    person_form.cleaned_data['person_id'])
            deceased_form_data.save()
            return HttpResponseRedirect('/crisis/')
        else:
            return render_to_response('person/deceased.html', {'deceased_form':deceased_form, 
                'person_form': person_form, 'error1':person_form, 'error2':deceased_form}, RequestContext(request))

    else:
        return render_to_response('person/deceased.html', {'deceased_form':DeceasedForm(), 
            'person_form': PersonForm()}, RequestContext(request))


 
def deceased_update(request, person_id):
    person_details = get_object_or_404(Person, person_id = person_id)
    deceased_details = get_object_or_404(Deceased, person_id = person_id)
    init_person = {'person_id' : person_details.person_id, 'person_name' : person_details.person_name, \
            'gender' : person_details.gender, 'age' : person_details.age , 'hair_color' : person_details.hair_color,\
            'wounds' : person_details.wounds, 'height' : person_details.height, 'identification_mark' : \
            person_details.identification_mark, 'color_complexation' : person_details.color_complexation 
            }
    init_deceased = {'latitude' : deceased_details.latitude, 'longitude' : deceased_details.longitude,\
            'idenitified'  : deceased_details.idenitified
            }
    if request.method == 'POST':
        person_update_form = PersonUpdateForm(request.POST)
        deceased_update_form = DeceasedUpdateForm(request.POST)
        valid_person_update_form = person_update_form.is_valid()
        valid_deceased_update_form = deceased_update_form.is_valid()

        if valid_person_update_form and valid_deceased_update_form:
            person_form_details = person_update_form.save(commit = False)
            deceased_form_details = deceased_update_form.save(commit = False)
            update_p = Person.objects.get(person_id = person_id)
            update_d = Person.objects.get(person_id = person_id)

            update_p.person_name = person_form_details.person_name
            update_p.gender = person_form_details.gender
            update_p.age = person_form_details.age
            update_p.hair_color = person_form_details.hair_color
            update_p.wounds = person_form_details.wounds
            update_p.height = person_form_details.height
            update_p.identification_mark = person_form_details.identification_mark
            update_p.color_complaxation = person_form_details.color_complexation

            update_d.latitude = deceased_form_details.latitude
            update_d.longitude = deceased_form_details.longitude
            update_d.idenitified = deceased_form_details.idenitified

            update_p.save()
            update_d.save()
            return HttpResponseRedirect('/crisis/')

        else:
            return render_to_response('person/deceased_update.html', {'deceased_form' : DeceasedUpdateForm(init_deceased),
                'person_form' : PersonUpdateForm(init_person)}, RequestContext(request))

    else:
        return render_to_response('person/deceased_update.html', {'deceased_form' : DeceasedUpdateForm(init_deceased),
            'person_form' : PersonUpdateForm(init_person)}, RequestContext(request))

    

#update will come here
def deceased_autocomplete(request):
    deceased_details = Deceased.objects.all()
    the_data=[]
    j=1;
    aaData ={}
    for i in deceased_details:
        aaData = {
            'person_name':i.person_id.person_name,
            'gender':i.person_id.gender,
            'age':i.person_id.age,
            'DT_RowId': 'row_' + str(j),
            }
        the_data.append(aaData)
        j=j+1
       
    the_data = json.dumps({
        'sEcho': 1,
        'iTotalRecords': j-1,
        'iTotalDisplayRecords': j-1,
        'aaData':the_data
    })
    return HttpResponse(the_data, content_type='application/json')

       
        
def deceased_list(request):
    """
    View to list all the deseased people in the diseaster area.

    """

    deceased_details = Deceased.objects.all()
    paginator = Paginator(deceased_details, 2)

    page = request.GET.get('page')
    try:
        deceased = paginator.page(page)
    except PageNotAnInteger:
        deceased = paginator.page(1)
    except EmptyPage:
        deceased = paginator.page(paginator.num_pages)

    return render_to_response('person/deceased_list.html', {'deceased':\
            deceased}, RequestContext(request))




def autocomplete(request):
    suggestions = []
    sqs = SearchQuerySet().autocomplete(person_id__startswith=request.GET.get('q',''))[:5]
    suggestions = [result.person_name for result in sqs]
    the_data = json.dumps({
        'results':suggestions
    })
    return HttpResponse(the_data, content_type='application/json')


def search_refugee(request):

    if request.method == 'POST':
        try:
            term = request.POST['q']
        except:
            return HttpResponseRedirect('/crisis/')

        results = SearchQuerySet().auto_query(term)
        names = []
        for r in results: 
            names.append(r.object)

        return render_to_response('search/search.html', {'result':names,'q':term}, RequestContext(request))
    else:
        return render_to_response('search/search.html', {}, RequestContext(request))



def refugee_to_decease(request):

    if request.method == 'GET':
        person_id = str(request.GET['q'])
        person_obj = get_object_or_404(Person, person_id=person_id)
        try:
            refugee_obj = Refugee.objects.get(person_id=person_obj)
            refugee_obj.delete()
            deceased = Deceased(person_id=person_obj)
            deceased.save()
            return HttpResponseRedirect('/crisis/')
        except:
            return HttpResponseRedirect('/crisis/')
    

def refugee_to_missing(request):
    
    if request.method == 'GET':
        person_id = str(request.GET['q'])
        person_obj = get_object_or_404(Person, person_id=person_id)
        try:
            refugee_obj = Refugee.objects.get(person_id=person_id)
            refugee_obj.delete()
            missing = Missing(person_id=person_obj)
            missing.save()
            return HttpResponseRedirect('/crisis/')
        except:
            return HttpResponseRedirect('/crisis/')


