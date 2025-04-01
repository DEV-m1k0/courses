from rest_framework import generics
from Subject.models import User
from .serializers import UserUsernameSerializer

class UsernameListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserUsernameSerializer