from crisis.models import User

def check_in_db(user):

    user_status = User.objects.all().filter(user_id=user)
    if user_status is not None:
        return True
    else:
        return False

