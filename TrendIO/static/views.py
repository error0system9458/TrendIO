from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView
from home.forms import HomeForm
from home.models import Post, Friend
from django.contrib.auth.models import User
import json
import urllib.request
import datetime
import requests
import time
from datetime import datetime
from accounts.models import UserProfile, Notification




class HomeView(ListView):

	template_name = 'home/home.html'


	#override the get method.
	def get(self, request):
		form = HomeForm()
		posts = Post.objects.all().order_by('-created')

		#NEED TO CHANGE THIS IMMEDIATELY TO GET LIMITED USERS.
		users = User.objects.exclude(id=request.user.id)

		userprofile = UserProfile.objects.get(user=request.user)

		notifications_set = Notification.objects.filter(user_id=request.user.id)

		logged_in_user = User.objects.get(id=request.user.id)

		#returns the instance user's friends as an object
		#if there is no friend, sorta passes, creates an instance and the create flag returns true.
		friend, created = Friend.objects.get_or_create(current_user=request.user)

		#creates a query set of every friend above and packs it into a variable.
		friends = friend.users.all()[:2]

		#generates time server info
		local_datetime = datetime.now()

		local_time = datetime.time(local_datetime)

		#Weather Info using open API
		#sets up url
		cityname = "New York"
		apikey = 'b860b36b88dbccda9c80a6d0b585d70d'
		units = 'imperial'
		sample_url = 'http://api.openweathermap.org/data/2.5/weather?q='
		complete_url = sample_url + cityname + '&mode=json&units=' + units + '&appid=' + apikey

		#opens site and decodes to utf8 encoding.
		open_site = urllib.request.urlopen(complete_url)
		site_data = open_site.read().decode('utf-8-sig')
		json_data = json.loads(site_data)

		#closes site to save resources
		open_site.close()

		#generates strings from json objects and arrays.
		city = json_data.get('name')
		main_info = json_data.get('main')

		# main_info = round(main_info_)
		temp_vals = [main_info['temp'], main_info['humidity'], main_info['temp_max']]
		data = json_data.get('weather')
		samp = data[0]
		country_data = json_data.get('sys')
		country = country_data['country']


		#round the temperature
		temp = round(main_info['temp'])

		#dict object stores all data.
		args = {
			'posts': posts,
			'form': form,
			'users': users,
			'logged_in_user':logged_in_user,
			'userprofile': userprofile,
			'friends': friends,
			'local_time': local_time,
			'city':city,
			'temp':temp,
			'sky':samp['description'],
			'icon': samp['icon'],
			'country': country,
			'notifications': notifications_set,
		}


		# print("\n", request.META, "\n")
		return render(request, self.template_name, args)

	def post(self,  request):
		if request.method=='POST':
			form = HomeForm(request.POST or None, request.FILES or None)
			if form.is_valid():
				post = form.save(commit=False)
				post.user = request.user
				post.save()
				text = form.cleaned_data['post']
				image = form.cleaned_data['image']

				args = {
				'form': form,
				'text': text,
				'image':image,
				}
				print('---------------------------------------------------------went thru------------------------------------------------------------')
				return render(request, self.template_name,args)
			#
			# return render(request, self.template_name, args )

		else:
			#for debug purposes
			print('else reached')
			form = HomeForm()
			args={
			'form':form
			}
			return render(request, 'home/home.html',args)



#under development @jul28.
def friendship_request(request, operation, pk):
	from_user = User.objects.get(id=request.user.id)
	to_user = UserProfile.objects.get(pk=pk)

	if operation == 'add':

		pass




def friendship_accept(request):
	from_user = User.objects.get(id=request.user.id)
	pass

def friendship_decline(request):
	pass




def change_friends(request, operation, pk):
	friend = User.objects.get(pk=pk)

	if operation == 'add':
		Friend.add_friend(request.user, friend)

	elif operation == 'remove':
		Friend.remove_friend(request.user, friend)
	return redirect('home:home')
