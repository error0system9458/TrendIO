from django.conf.urls import url
from home.views import HomeView
from . import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'

urlpatterns = [
	path('', HomeView.as_view() , name="home"),
	path('connect/<operation>/<int:pk>/', views.change_friends, name='change_friends'),
	path('connect/<operation>/<int:pk>/', views.friendship_request, name='friendship_request'),

	# path('/post/media/', CreateView.as_views(). name="home_create_post"),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
