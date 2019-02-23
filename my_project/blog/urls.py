#handles url redirections

from django.urls import path
from . import views #imports view.py  (dot is corrent directory)

urlpatterns = [
	path('', views.home, name='blog-home'),
    path('blog/', views.home, name='blog-home') ,	
    path('about/', views.about, name='blog-about')
]	#for home page leave path empty