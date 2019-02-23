from django.shortcuts import render		# to render http page in a shortcut
#from django.http import HttpResponse

from .models import Post 		#imports database model


# #dummy data
# posts=[
# # dictionary
# 	{
# 		'author': 'Tanzilur Rahman',
# 		'title': 'Blog Post 1',
# 		'content': 'First post content',
# 		'date_posted': 'August 69, 2019'
# 	},
# 	{
# 		'author': 'Omair Khan',
# 		'title': 'Blog Post stupid',
# 		'content': 'First post by stupid',
# 		'date_posted': 'August 41, 2019'
# 	},
# 	{
# 		'author': 'Daniyal Abbasi',
# 		'title': 'Entitlement',
# 		'content': 'First whine',
# 		'date_posted': 'August 42, 2019'
# 	}

# ]

#fuction to take request arguments
def home(request):
	context = {
		'posts': Post.objects.all()		# template will access dummy data via key within ''
	}
	return render(request, 'blog/home.html', context)		# has to return http response or exception
	#passed 3rd var has to be a dictionary
	#context is useless now since we're using database models
# Create your views here.


def about(request):
	return render(request, 'blog/about.html', {'title': 'Passed Title'})
