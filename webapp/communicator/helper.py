"""
Filename: communicator/helper.py
Authors: Bithin Alangot Seshagiri Prabhu Harish Navnit
Copyright: Wise Earth Technology
This file is part of the CrisisCommunicator Project.  
It is licensed under the Peaceful Open Source License.  
Please see the license terms in PeaceOSL.txt
"""
from crisis.models import User

def check_in_db(user):

    user_status = User.objects.all().filter(user_id=user)
    if user_status is not None:
        return True
    else:
        return False

