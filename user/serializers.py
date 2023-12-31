from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validate_data):
        password = validate_data.pop('password', None)
        instance = self.Meta.model(**validate_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    



############ User Profile Serializer #############

class UserPorfileSerializer(serializers.ModelSerializer):

    profile_image = serializers.ImageField(
        max_length =None,
        use_url = True
    )

    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['user', 'first_name', 'last_name', 'bio', 'username', 'profile_image']
