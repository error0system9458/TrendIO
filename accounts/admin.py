from django.contrib import admin
from accounts.models import UserProfile

# Register your models here.

#this custom class inherits from the default admin model


class UserProfileAdmin(admin.ModelAdmin):

	#
	list_display = ('user', 'user_info', 'social_score')

	def user_info(self, obj):
		return obj.social_score




admin.site.register(UserProfile, UserProfileAdmin)
