from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.response import Response
from rest_framework import status

from drf_spectacular.utils import extend_schema

from accounts.serializers.account_edit import AccountEditSerializer # noqa
from accounts.models import User # noqa


@extend_schema(
    tags=['Users'],
    description='Editing account page if user is patient.'
)
class AccountEditView(UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = AccountEditSerializer
    queryset = User.objects.all()
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance, created = User.objects.update_or_create(
            email=serializer.validated_data.get('email', None),
            defaults=serializer.validated_data
        )
        serializer.update(instance, serializer.validated_data)
        return Response(status=status.HTTP_200_OK)
