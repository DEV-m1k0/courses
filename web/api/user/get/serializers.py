from rest_framework import serializers
from Subject.models import User

class UserUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )