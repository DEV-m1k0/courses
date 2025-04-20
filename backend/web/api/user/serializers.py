from Subject.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        if "password" in validated_data:
            password: str = validated_data['password']
            instance: User = super().create(validated_data)
            instance.set_password(password)
            return instance
        return super().create(validated_data)