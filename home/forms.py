from django import forms
from home.models import Post

class HomeForm(forms.ModelForm):
	post = forms.CharField(widget=forms.TextInput(
		attrs={
		'class': 'form-control',
		'placeholder' : 'What are you feeling right now?'
		}
	))

	image = forms.FileField(widget=forms.FileInput())

	class Meta:
		model = Post
		fields = ('post','image',)

#
# class CreatePost(forms.ModelForm):
# 	image_post = forms.ImageField(upload_to='/media/image_posts')
#
# 	class Meta:
#
# 		model = Post
