"""
Filename: person/models.py
Authors: Bithin Alangot Seshagiri Prabhu Harish Navnit
Copyright: Wise Earth Technology
This file is part of the CrisisCommunicator Project.  
It is licensed under the Peaceful Open Source License.  
Please see the license terms in PeaceOSL.txt
"""
from django.db import models

from crisis.models import Global, Comment
from refugeecenter.models import RefugeeCenter

GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
)

WOUND_CHOICES = (('Wounded', 'Wounded'), ('No Wounds', 'No Wounds'))

IDENTIFIED = (('Y', 'Person Identified'), ('N', 'Person not yet identified'))

class Person(models.Model):
    """
    Store the details of all the people in the disaster zone.

    Person ID : If they have a ID card or Any ID details or one generated 

    """

    person_id = models.CharField(max_length=100, primary_key=True)
    person_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(choices=GENDER, max_length=10, default='M')
    age = models.IntegerField(blank=True, null=True)
    hair_color = models.CharField(max_length=100, null=True, blank=True)
    wounds = models.CharField(choices=WOUND_CHOICES, max_length=10, default='Wounded')
    height = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    identification_mark = models.CharField(max_length=100, blank=True, null=True)
    color_complexation = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'crisis_person'

        def __unicode__(self):
            return self.person_name


class Refugee(models.Model):
    """ 
    Details of a Refugee

    """
    
    person_id = models.ForeignKey(Person)
    center_id = models.ForeignKey(RefugeeCenter, blank=True, null=True)
    gid = models.ForeignKey(Global, blank=True, null=True)
    health_status = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'crisis_refugee'
        unique_together = ('person_id','center_id')


class Missing(models.Model):
    """
    Details of the people who goes missing in the disaster

    """
    
    missing_id = models.CharField(max_length=10, primary_key=True)
    person_id = models.ForeignKey(Person)
    gid = models.ForeignKey(Global, blank=True, null=True)
    last_seen = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'crisis_missing'


class Deceased(models.Model):
    """
    Details of Deceased people in the disaster

    """

    person_id = models.ForeignKey(Person)
    latitude = models.DecimalField(blank=True, null=True,max_digits=19, 
                    decimal_places=10)
    longitude = models.DecimalField(blank=True, null=True,max_digits=19, 
                    decimal_places=10)
    gid = models.ForeignKey(Global, blank=True, null=True)
    idenitified = models.CharField(choices=IDENTIFIED, max_length=20, default='Y')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'crisis_deceased'


