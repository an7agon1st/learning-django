from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	"""docstring for UserRegisterForm"""
	email = forms.EmailField(required = True)		# compulsary field

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):		# update user db instance
	email = forms.EmailField(required = True)		# compulsary field

	class Meta:
		model = User
		fields = ['username', 'email']	

class ProfileUpdateForm(forms.ModelForm):		# Update profile info
	"""docstring for ProfileUpdateForm"""
	class Meta:
		model = Profile
		fields = ['image']		# update profile image
		
