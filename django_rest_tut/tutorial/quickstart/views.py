from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API END POINT THAT ALLOWS USER TO BE VIEWED OR EDITED
    """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API ENDPOINT THAT ALLOWS GROUPS TO BE VIEWED OR EDITED
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Create your views here.




