from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.tokens import default_token_generator
from rest_framework import serializers

from accounts.utils import decode_uid # noqa

UserModel = get_user_model()


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
<<<<<<< HEAD
=======
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    phone_num = serializers.CharField(write_only=True)
>>>>>>> 2a67131b69271284b976cb5304854fdb0c03f3d6
    password = serializers.CharField(write_only=True, validators=[validate_password])

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            email=validated_data['email'],
<<<<<<< HEAD
=======
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_num=validated_data['phone_num'],
>>>>>>> 2a67131b69271284b976cb5304854fdb0c03f3d6
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = UserModel
<<<<<<< HEAD
        fields = ("id", "email", "password",)
=======
        fields = ("id", "email", "password", 'first_name', 'last_name', 'phone_num')
>>>>>>> 2a67131b69271284b976cb5304854fdb0c03f3d6


class ConfirmRegistrationSerializer(serializers.Serializer):
    uid = serializers.CharField(write_only=True)
    token = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user_model = get_user_model()
        uid = attrs['uid']
        token = attrs['token']

        try:
            user = user_model.objects.get(pk=decode_uid(uid))
        except (user_model.DoesNotExist, ValueError, TypeError, OverflowError):
            raise serializers.ValidationError(
                {'uid': _('Invalid uid')},
                code='invalid_uid',
            )

        if not default_token_generator.check_token(user, token):
            raise serializers.ValidationError(
                {'token': _('Invalid token')},
                code='invalid_token',
            )

        attrs['user'] = user

        return attrs

    def create(self, validated_data):
        user = validated_data['user']
        user.is_confirmed = 1
        user.save(update_fields=('is_confirmed',))
        return user

