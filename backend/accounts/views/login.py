from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from accounts.serializers.login import LoginSerializer # noqa


@extend_schema(
    tags=['Users'],
)
class LoginView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = []
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(
            data=self.request.data,
            context={'request': self.request}
        )
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            return Response(None, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)
