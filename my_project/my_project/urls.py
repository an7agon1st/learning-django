"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 		#include tells django what patterns will route to blog urls
from users import views as user_views
from django.contrib.auth import views as auth_views     # import login logout views
from django.conf import settings                # copied from django static
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name = 'register'),
    path('profile/', user_views.profile, name = 'profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout'),  #argument in as view tells where to look for login logout template
    # for log in log out
    path('', include('blog.urls'), name='App-Blog'),	#\blog link maps to blog.url (includes blog app's urls)
]		#include fuction chops the url we're at and sends the remaining string. (chops /blog and sends the rest)


if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)        # allows media to work within browser. Read django doc
