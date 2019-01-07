from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.forms import ModelForm
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
	#defining fields
	first_name = forms.CharField(max_length=40)
	last_name = forms.CharField(max_length=40)

	#defining fields wanted to be filled out in the registration
	class Meta:
		model = User
		fields = ('username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2'
		)


	#saves the registration data to the database
	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()
			print('User Creation Successful!')
		return user



class EditProfileForm(UserChangeForm):

	class Meta:
		model = User
		fields = (
			'first_name',
			'last_name',
			'password',

		)

# model form for profile photo upload

class ProfilePhotoForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ('image',)


class ChangePasswordForm(UserChangeForm):

	class Meta:
		model = User
		fields = ('password',)
