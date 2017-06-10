from django.contrib.auth import get_user_model
from rest_framework import generics

from auth.serializers import UserSerializer


class UserRegistrationView(generics.ListCreateAPIView):
    permission_classes = ['AllowAny',]
    serializer_class = UserSerializer
    queryset = get_user_model().objects
