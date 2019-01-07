from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditProfileForm, ProfilePhotoForm
from django.contrib.auth.models import User
from .forms import *
from .models import UserProfile, Notification
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_object_or_404
from .models import UserProfile
from django.views.generic.list import ListView
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
import os
import urllib
import json



class ProfileView(ListView):

	template_name = 'templates/profile.html'

	def get(self, request, pk=None):

		is_liked = False

		if pk:

			user = User.objects.get(pk=pk)
			userprofile = UserProfile.objects.get(pk=pk)

			#if a record exists for a like by request.user to user, is_liked is true
			if userprofile.profile_likes.filter(id=request.user.id).exists():
				is_liked = True

			args={
				'user': user,
				'userprofile': userprofile,
				'is_liked': is_liked,
			}

		else:

			user = request.user
			userprofile = UserProfile.objects.get(user=request.user)
			notifications_set = Notification.objects.filter(user_id=request.user.id)
			args = {
				'user':user,
				'userprofile': userprofile,
				'notifications_set': notifications_set,
			}


		return render(request, 'accounts/profile_test.html', args)





def register(request):

	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account/login')

	else:
		form = RegistrationForm()
		args = {'form': form}
		return render(request,'accounts/reg_form.html',args)



def profile(request, pk=None):

	storage = messages.get_messages(request)
#this view is under development as of now.
	is_liked = False

	#for viewing others profiles
	if pk:
		#initializes both variables if a primary key is found

		userprofile = UserProfile.objects.get(pk=pk)
		user=User.objects.get(pk=pk)
		notifications_set = Notification.objects.filter(user_id=user.id)

		#if a record exists for a like by request.user to user, is_liked is true
		if userprofile.profile_likes.filter(id=request.user.id).exists():
			is_liked = True

		user = User.objects.get(pk=pk)
		args={
			'user': user,
			'userprofile': userprofile,
			'is_liked': is_liked,
			'notifications':notifications_set,
		}



	#to view request.user profile
	else:
		user=request.user
		userprofile= UserProfile.objects.get(user=request.user)


		args={
			'user': request.user,
			'userprofile': userprofile,
			'message' : storage
		}

	if request.user.is_authenticated:
		#profile contains all the info about the logged in user

		return render(request, 'accounts/profile.html', args)

		#tries for registered user.

	else:
		return render(request,'accounts/login.html')

#REQUIRED A VIEW FOR VIEWING A PROFILE OTHER THAN REQUEST.USER

#removed all hardcoded urls



def edit_profile(request):

	#checks if user is logged in
	if request.user.is_authenticated:

		#checks if the request method is POST
		if request.method=='POST':

			#creats new EditProfileForm instance and named it form.
			form = EditProfileForm(request.POST, instance=request.user)

			#checks for adulterated data.
			if form.is_valid():

				#saves the new data and redirects back to profile page.
				form.save()
				return redirect('accounts:profile')

		else:
			form = EditProfileForm(instance=request.user)
			args = {
				'form':form
			}
			return render(request, 'accounts/edit_profile.html', args)

	else:
		return render(request, 'accounts/login.html')
	#testing

def change_password(request):
	storage = messages.get_messages(request)
	if request.user.is_authenticated:
		if request.method=='POST':
			form = PasswordChangeForm(data=request.POST, user=request.user)
			if form.is_valid():
				form.save()
				messages.success(request, "Your new password has been saved successfully.")
				update_session_auth_hash(request, form.user)

				return redirect('accounts:profile')
			else:
				return redirect('accounts:change_password')
		else:
			messages.warning(request,"Check your info.")
			form = PasswordChangeForm(user=request.user)
			args = {
				'form':form,
				'message' : storage
			}
			return render(request, 'accounts/change_password.html', args)
	else:
		return render(request, 'accounts/login.html')


def about_us(request):

	return render(request, 'accounts/about_us.html')

def music(request):

	return render(request,'accounts/music.html')


def photos(request, pk=None):


	if request.user.is_authenticated and request.method=='GET':
		user = User.objects.get(pk=request.user.id)

		args = {'user':user}

	else:
		user = User.objects.get(pk=pk)
		args = {'user':user}


	return render(request, 'accounts/photos.html',args)

def like_user(request):

	user = get_object_or_404(UserProfile, id=request.POST.get('userprofile'))

	is_liked = False
	if user.profile_likes.filter(id=request.user.id).exists():
		user.profile_likes.remove(request.user)
		is_liked = False

	else:
		user.profile_likes.add(request.user)
		is_liked = True
	return redirect('home:home')


def like_post(request):
	return redirect('home:home')

def search_results(request):

	#gets the query from the input in search form in template
	search_query = request.GET.get("q")
	if request.method == "GET" and search_query != "":
		#returns a response with matching queries
		users = User.objects.filter(username__startswith=search_query)

		args = {
			'users':users,
			'search_query': search_query,

			}
		return render(request, 'accounts/search_results.html',args)

	else:
		empty_search_message = "Please Type Something in the Search."
		args = {
			'empty_search_message':empty_search_message,
			'search_query':search_query,
			}

		return render(request, 'accounts/search_results.html',args)

		
#This view isnt useful and should be removed. Also maybe a bug.
def get_all_users(request):
	user_list = User.objects.all()

	args= {
		'user_list': user_list,
	}
	return render(request, 'accounts/all_users', args)


#uploads an image file to the server requested by an authenticated user.
def profile_photo_upload(request):
	instance = get_object_or_404(UserProfile, id=request.user.id)

	if request.method == 'POST':
		form = ProfilePhotoForm(request.POST, request.FILES, instance=instance)
		if form.is_valid():
				instance = form.save(commit=False)
				instance.user = request.user
				instance.save()
				return redirect('accounts:profile')

	else:
			form = ProfilePhotoForm()
			return render(request, 'accounts/photo_upload.html', {'form':form})
