"""
Filename: communicator/forms.py
Authors: Bithin Alangot Seshagiri Prabhu Harish Navnit
Copyright: Wise Earth Technology
This file is part of the CrisisCommunicator Project.  
It is licensed under the Peaceful Open Source License.  
Please see the license terms in PeaceOSL.txt
"""
from django.forms import ModelForm
from django import forms
#from django.core import Validator
from django.shortcuts import get_object_or_404

from crisis.models import User

import re

def check_alphanumeric(name):
    if re.match("^[A-Za-z0-9 ]*$",name):
        return True
    else:
        return False


class UserEnterForm(ModelForm):

    """
    This form will be display in the starting page.

    If the user is using it for the first time, he will

    be prompt to enter a few details.

    All feilds are not compelsory

    rtype: HTML form 

    """

    class Meta:
        model = User
        exclude = ('internal_id', 'role', 'gender', 'health_status')
        widgets = {
            'user_id': forms.TextInput(attrs={'placeholder':'User ID'}),
            'name': forms.TextInput(attrs={'placeholder':'Name'})
        }

    
    def clean_user_id(self):
        user_id = self.cleaned_data['user_id']
        if check_alphanumeric(user_id):
            return user_id
        else:
            raise forms.ValidationError("Only alpha numeric possible")


class UserRegisterForm(ModelForm):

    """
    A user can register to a Crisis Communicator, once a user is register

    with once communicator, he can use it any other communicator. 

    rtype: HTML form

    """

    class Meta:
        model = User
        exclude = ('internal_id')
        widgets = { 
            'user_id': forms.TextInput(attrs={'placeholder': 'User ID'}),
            'role': forms.RadioSelect(),
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
			'gender': forms.RadioSelect(),
            'health_status': forms.TextInput(attrs={'placeholder': 'Health Status'}),
        }

    def clean_user_id(self):
        user_id = self.cleaned_data['user_id']
        if check_alphanumeric(user_id):
            return user_id
        else:
            raise forms.ValidationError("Only Alphanumeric possible")

