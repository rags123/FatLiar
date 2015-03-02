import datetime
from django import forms
from site_one.models import Blog
from django.contrib.auth.models import User
from site_one.models import UserProfile

class BlogForm(forms.ModelForm):
	title = forms.CharField(max_length=120, help_text='Please enter the title.')
	content = forms.CharField(widget=forms.Textarea, help_text='Add content to the title.')
	posted = forms.DateField(widget=forms.HiddenInput(), initial=datetime.date.today())
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	class Meta:
		model = Blog

class UserForm(forms.ModelForm):
	first_name = forms.CharField(help_text='Please enter your first name.')
	last_name = forms.CharField(help_text='Please enter your surname.')
	username = forms.CharField(help_text='Please enter a username.')
	email = forms.CharField(help_text='Please enter email.')
	password = forms.CharField(widget=forms.PasswordInput(), help_text='Please enter your password.')

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
	website = forms.URLField(help_text='Please enter your website.', required=False)
	picture = forms.ImageField(help_text='Select a profile image.', required=False)

	class Meta:
		model = UserProfile
		fields = ['website', 'picture']