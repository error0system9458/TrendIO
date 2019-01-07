from django.conf.urls import url
from home.views import HomeView
from .views import PostRudView
from django.urls import path


app_name = 'home'

urlpatterns = [
	path('', HomeView.as_view() , name="home"),
	path('post/<int:pk>/', PostRudView.as_view(), name='post-rud'),

]
