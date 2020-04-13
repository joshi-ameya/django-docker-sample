from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('created_at', 'updated_at',)
        read_only_fields = ('id', )
        write_only_fields = ('password',)
