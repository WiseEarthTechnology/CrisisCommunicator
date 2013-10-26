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
