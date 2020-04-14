from django.contrib.auth import login
from rest_framework import permissions as rest_permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from knox.views import LoginView as KnoxLoginView

from user.models import User
from utils.drf.views import ModelCRUViewSet
from .. import serializers


class UserLoginView(KnoxLoginView):
    """
    An endpoint for user login.
    """
    permission_classes = (rest_permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return super(UserLoginView, self).post(request, format=None)


class UserViewSet(ModelCRUViewSet, ):
    """
    A simple ViewSet for viewing and editing the accounts
    associated with the user.
    """
    permission_classes = (rest_permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    @action(methods=('get',), detail=False)
    def me(self, request):
        serializer = serializers.UserSerializer(request.user)
        serializer_data = serializer.data
        return Response(serializer_data, status=200)
