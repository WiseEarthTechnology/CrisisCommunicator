"""
Filename: refugeecenter/models.py
Authors: Seshagiri Prabhu
Copyright: Wise Earth Technology
Credits : Bithin Alangot
This file is part of the CrisisCommunicator Project.  
It is licensed under the Peaceful Open Source License.  
Please see the license terms in PeaceOSL.txt
"""
from django.db import models

from crisis.models import Global, TrackCommunicator


class RefugeeCenter(models.Model):

    """
    Stores all the details regarding a refugee camp.

    Population: Number of people Currently, residing in the camp.
    supplies_available_for: For how many days the resources are available.
    """
    
    center_id = models.CharField(max_length=50, primary_key=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.DecimalField(blank=True, null=True,max_digits=19, 
                    decimal_places=10)
    longitude = models.DecimalField(blank=True, null=True,max_digits=19, 
                    decimal_places=10)
    gid = models.ForeignKey(Global, blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    population_capacity = models.IntegerField(blank=True, null=True)
    supplies_available_for = models.IntegerField(blank=True, null=True)

    class Meta: 
        db_table = 'crisis_refugeecenter'

    def __unicode__(self):
        return self.place



