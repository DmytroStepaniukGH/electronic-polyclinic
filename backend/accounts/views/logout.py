from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import logout

from drf_spectacular.utils import extend_schema


@extend_schema(
    tags=['Users'],
)
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': "Logout successful"})
