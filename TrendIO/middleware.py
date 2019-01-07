#writing custom middleware for login required.

#regular expression import
import re
from django.urls import reverse
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout

#strips the slash and returns the path without the first slash
EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]


if hasattr(settings, 'LOGIN_EXEMPT_URL'):

	#adds to the list for every path in login_exempt_url list in settings.
	EXEMPT_URLS += [re.compile(path) for path in settings.LOGIN_EXEMPT_URL]

class LoginRequiredMiddleware:

	#instance get_response
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)
		return response

	#takes self obviously, view_func is the same functions in the views and the function gets passed in before processing the view itself.
	def process_view(self, request, view_func, view_args, view_kwargs):

		#checks if user exists in the request object int he request object.
		assert hasattr(request, 'user')

		#request has a path object
		path = request.path_info.lstrip('/')

		#if not request.user.is_authenticated:
		#	if not any(url.match(path) for url in EXEMPT_URLS):
		#		return redirect(settings.LOGIN_URL)

		#if url the user is requesting is in the exempt urls
		url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

		#bug: loading logout even without the statement below.
		if path==reverse('accounts:logout').lstrip('/'):
			logout(request)

		#send logged in user to LOGIN_REDIRECT_URL if request contains any exempt urls
		if request.user.is_authenticated and url_is_exempt:
			return redirect(settings.LOGIN_REDIRECT_URL)

		#return none if they are logged in or the url is in the exempt list
		elif request.user.is_authenticated or url_is_exempt:
			return None
		

		#redirect user if they arent logged in to the login page.
		else:
			return redirect(settings.LOGIN_URL)

