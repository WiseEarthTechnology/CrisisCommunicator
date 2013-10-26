from django.shortcuts import get_object_or_404

from models import Global, TrackCommunicator
import datetime

def generate_gid():
    
    """
    Method to generate Global ID for each message that is generated in the 
    Crisis Communicator. 
    
    rtype:Global Object

    """

    _internal_id = get_object_or_404(TrackCommunicator, internal_id='amrita')
    time_stamp= str(datetime.datetime.now())[11:].replace(":","").replace(".","")
    generate_id=time_stamp+(str(_internal_id))
    gid_data = Global(gid=generate_id, internal_id=_internal_id, csv_update='a',\
                        response_status=False)
    gid_data.save()
    
    return get_object_or_404(Global, gid=generate_id)





