"""
Filename: resources/forms.py
Authors: Bithin Alangot Seshagiri Prabhu Harish Navnit
Copyright: Wise Earth Technology
This file is part of the CrisisCommunicator Project.  
It is licensed under the Peaceful Open Source License.  
Please see the license terms in PeaceOSL.txt
"""
from django.forms import ModelForm
from django import forms

from models import Resource
from refugeecenter.models import RefugeeCenter

class ResourceForm(ModelForm):
    """
    Return a empty form to enter the resource details. 

    rtype: HTML Form 

    """

    class Meta: 
        model = Resource
        exclude = ('gid', 'comment', 'supply', 'supply_required')
        widgets = {
            'resource_id': forms.TextInput(attrs={'placeholder':'Resource ID'}),
            'resource_name': forms.TextInput(attrs={'placeholder':'Enter the name of the resource'}),
            'location': forms.TextInput(attrs={'placeholder':'Location'}),
            'latitude': forms.TextInput(attrs={'placeholder':'Latitude'}),
            'longitude': forms.TextInput(attrs={'placeholder':'Longitude'}),
            'resource_type': forms.TextInput(attrs={'placeholder':'Enter the type of resource'}),
                }
    
    def __init__(self, *args, **kwargs):
        super(ResourceForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['refugee_center'].queryset = RefugeeCenter.objects.all()
            self.fields['refugee_center'].empty_label = "Select a Refugee Center"
            self.fields['refugee_center'].widget.choices = self.fields['refugee_center'].choices


