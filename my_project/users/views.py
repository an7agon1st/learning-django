from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm		#default form by django
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm		#custom form created at forms.py, UserUpdate and profileUpdate allows upiating forms
from django.contrib.auth.decorators import login_required

def register (request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)	# request.POST passes POST data to the form
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')	#cleaned data converts data into python types from form
			#messages display once, and diappear in the next get request
			messages.success(request, f'Account created for {username}!, Log in')
			return redirect('login')


	else:
		form = UserRegisterForm()	#converts a form into html
	return render(request, 'users/register.html', {'form':form})	#renders the form to html template register.html, passes form as context

# Create your views here.

#types of messages
# messages.debug
# messages.success
# messages.info
# messages.warning
# messages.error

@login_required
def profile(request):
	if request.method == 'POST':	# create instance of UserUpdate and ProfileUpdate

		# create instance of UserUpdate and ProfileUpdate
		u_form = UserUpdateForm(request.POST, instance = request.user)		# request.POST passes post data to the form
		# parameter passes current user to show in form
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile) # request.FILES sends the file (image)
		#pass this ^ to template via context

		if u_form.is_valid() and p_form.is_valid(): 		#checks if forms are valid
			u_form.save()
			p_form.save()
			messages.success(request, f'Account Updated') # give a success message
			return redirect('profile')		# to stop browser from sending another POST, instead sends GET msg

	else:
		u_form = UserUpdateForm(instance = request.user)		# parameter passes current user to show in form
		p_form = ProfileUpdateForm(instance = request.user.profile)

	context = {
		'u_form' : u_form,
		'p_form' : p_form
	}

	return render(request, 'users/profile.html', context)

