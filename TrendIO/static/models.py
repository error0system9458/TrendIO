from django.db import models
from django.contrib.auth.models import User
from accounts.models import Notification





#skeleton for a post
class Post(models.Model):
	post = models.CharField(max_length=150)
	image = models.FileField(upload_to='photo_posts', null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.user.username
		return self.post






class Friend(models.Model):

	#users that logged in user is friends with
	users = models.ManyToManyField(User)
	#creates a current_user instance of the User
	current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)
	request_accept = models.BooleanField(default=True)



	@classmethod
	def friend_request(cls, current_user, new_friend):
		friend, created = cls.objects.get_or_create(

		#returns the instance of the User aka current logged in user.
		current_user = current_user

		)
		print(friend)
		


	@classmethod
	#adds a friend
	def add_friend(cls, current_user, new_friend):
		friend, created = cls.objects.get_or_create(

		#returns the instance of the User aka current logged in user.
		current_user = current_user

		)
		friend.users.add(new_friend)
		Notification.objects.create(user=current_user,notification_description="{} added: {}".format(current_user, new_friend))



	#removes a friend
	@classmethod
	def remove_friend(cls, current_user, new_friend):
		friend, created = cls.objects.get_or_create(

		#returns the instance of the User aka current logged in user.
		current_user = current_user
		)
		friend.users.remove(new_friend)
		Notification.objects.create(user=current_user,notification_description="{} Friend Deleted: {}".format(current_user, new_friend))
