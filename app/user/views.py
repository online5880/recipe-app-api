"""
Views for the user API
"""

from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """사용자 생성"""

    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    "새로운 인증토큰 생성"
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        "인증된 사용자 반환"
        return self.request.user
