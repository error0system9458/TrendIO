
#Friend Management System v1

from django.contrib.auth.models import User
from home.models import Friend




def receive_request(current_user, new_friend):
    user = User.objects.get(id=request.user.id)
    new_friend = Friend.
