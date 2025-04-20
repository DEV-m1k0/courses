from .serializers import UserSerializer
from rest_framework import generics
from Subject.models import User



class UserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer