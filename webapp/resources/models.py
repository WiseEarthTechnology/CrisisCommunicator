"""
Filename: resources/models.py
Authors: Bithin Alangot Seshagiri Prabhu Harish Navnit
Copyright: Wise Earth Technology
This file is part of the CrisisCommunicator Project.  
It is licensed under the Peaceful Open Source License.  
Please see the license terms in PeaceOSL.txt
"""
from django.db import models
from refugeecenter.models import RefugeeCenter
from crisis.models import Global, Comment


class Supply(models.Model):
    """
    quantity of resource available

    """
    
    quantity = models.IntegerField(null=True, blank=True)
    measurement = models.CharField(max_length=10, null= True, blank=True)

    class Meta: 
        db_table = 'crisis_supply'


class Resource(models.Model):
    """
    Details of various resources that are available in the disaster area.

    """

    resource_id = models.CharField(max_length=50, primary_key=True)
    resource_name = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.DecimalField(blank=True, null=True, max_digits=19, 
                    decimal_places=10)
    longitude = models.DecimalField(blank=True, null=True, max_digits=19, 
                    decimal_places=10)
    
    gid = models.ForeignKey(Global, blank=True, null=True)
    resource_type = models.CharField(max_length=100, blank=True, null=True)
    supply = models.ForeignKey(Supply, blank=True, null=True, related_name='current_supply')
    supply_required = models.ForeignKey(Supply, blank=True, null=True, related_name='required_supply')
    refugee_center = models.ForeignKey(RefugeeCenter, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, blank=True, null=True)

    class Meta:
        db_table = 'crisis_resource'

    def __unicode__(self):
        return self.location

