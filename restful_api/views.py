from django.contrib.auth.models import User
from rest_framework import generics, permissions

from .serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    """ List view for User model - get/post """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Detail view for User model - get/put/delete """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

