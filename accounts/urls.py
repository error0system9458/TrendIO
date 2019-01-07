from django.urls import path
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from . import views
from .views import ProfileView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'accounts'

urlpatterns = [

	path('login/' , login, {'template_name': 'accounts/login.html'}, name='login'),
	path('logout/', logout, {'template_name':'accounts/logout.html'}, name='logout'),
	path('register/', views.register, name="register"),
	path('profile/', views.profile, name="profile"),
	path('profile/<int:pk>/', views.profile, name="profile_pk"),
	path('profile/edit_profile/', views.edit_profile, name="edit_profile"),
	path('profile/change_password/', views.change_password, name="change_password"),
	#all args that reset-password system takes are passed
	path('reset-password/', password_reset, {'template_name': 'accounts/reset_password.html', 'post_reset_redirect': 'accounts:password_reset_done', 'email_template_name': 'accounts/reset_password_email.html'}, name='reset_password'),
	path('reset-password/done/', password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'),
	path('reset-password/confirm/<uidb64>/<token>/', password_reset_confirm, {'template_name': 'accounts/reset_password_confirm.html', 'post_reset_redirect': 'accounts:password_reset_complete'}, name='password_reset_confirm'),
	path('reset-password/complete/', password_reset_complete, {'template_name': 'accounts/reset_password_complete.html'}, name='password_reset_complete'),
	path('about_us/', views.about_us, name="about_us"),
	path('profile/music/', views.music, name="music"),

	#photo gallery feature June 29, 2018.
	path('profile/photos/', views.photos, name="photos"),
	path('profile/<int:pk>/photos/' ,views.photos, name="photos_pk"),
	path('search_results/' , views.search_results, name="search_results"),
	path('like_user/', views.like_user, name="like_user"),

	#uploading profile photos
	path('profile/profile_photo_upload/', views.profile_photo_upload , name="profile_photo_upload"),
	path('profile_test/', ProfileView.as_view(), name='profile_test'),
	path('profile_test/<int:pk>/', ProfileView.as_view(), name='profile_test_pk')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
