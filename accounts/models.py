from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
from django.shortcuts import reverse
from django.utils.translation import gettext as _


class UserProfileManager(models.Manager):

	def get_queryset(self):
		return super(UserProfileManager, self).get_queryset().filter(city="")

	#returns a queryset of all registered users



class Notification(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE )
	notification_description = models.CharField(max_length=100, null=True, default="No Notifications", blank=True)


	def __str__(self):
		return self.notification_description


class UserProfile(models.Model):
	
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.CharField(max_length=100, null=True, blank=True)
	image = models.ImageField(upload_to='profile_photo', default="", blank=True)
	city = models.CharField(max_length=100, default='', blank=True)
	instagram_name = models.CharField(max_length=20, default='',blank=True)
	snapchat_name = models.CharField(max_length=20, default='',blank=True)
	social_score = models.DecimalField(default=5,max_digits=2, decimal_places=1)
	photo_likes = models.IntegerField(default=0)
	profile_likes = models.ManyToManyField(User, related_name='profile_likes', blank=True)
	notifications = models.CharField(max_length=100, default='No Notifications', null=True, blank=True)
	# friend_requests = models.ManyToManyField()
 



	def get_absolute_url(self):
		return reverse('accounts:profile', kwargs={'pk':self.pk})

	def __str__(self):
		return self.user.username
		return self.UserProfile.profile_likes

class UserGallery(models.Model):
	photos = models.ImageField(upload_to='photo_gallery', blank=True)


def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])



post_save.connect(create_profile, sender=User)
