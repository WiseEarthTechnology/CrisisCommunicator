"""
Filename: crisis/forms.py
Authors: Seshagiri Prabhu 
Copyright: Wise Earth Technology
Credits : Bithin Alangot
This file is part of the CrisisCommunicator Project.  
It is licensed under the Peaceful Open Source License.  
Please see the license terms in PeaceOSL.txt
"""
from django.forms import ModelForm
from django import forms 

from crisis.models import Comment
import re

class CommentForm(ModelForm):
    """
    Return a empty form to enter the comment. 

    rtype: HTML Form 

    """

    class Meta: 
        model = Comment
        exclude = ('user_id', 'comment_id')
        widgets = {
				'comment': forms.Textarea(attrs={'placeholder':'Enter Your Comments here', 'cols': 10, 'rows': 5}),
        }
