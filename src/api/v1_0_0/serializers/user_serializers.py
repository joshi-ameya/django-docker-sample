from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from user.models import User


class UserLoginSerializer(serializers.ModelSerializer):
    """
    User Authentication Serializer
    """
    email = serializers.EmailField(required=True, allow_blank=False)

    class Meta:
        model = User
        fields = ('email', 'password', )
        extra_kwargs = {'password': {'write_only': True, }}

    def validate(self, data):
        """
            User Authentication
        """
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise AuthenticationFailed(detail=_('Invalid Credentials'))
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at', )
        extra_kwargs = {'password': {'write_only': True, }}
