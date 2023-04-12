from rest_framework import serializers

from accounts.models import User # noqa


class AccountEditSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    patronim_name = serializers.CharField(max_length=150)
    birth_date = serializers.CharField(max_length=8)
    sex = serializers.CharField()
    email = serializers.EmailField()
    phone_num = serializers.CharField(max_length=13)
    address_city = serializers.CharField(max_length=50)
    address_street = serializers.CharField(max_length=150)
    address_house = serializers.CharField(max_length=10)
    address_appartment = serializers.CharField(max_length=10)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'patronim_name',
            'birth_date',
            'sex',
            'email',
            'phone_num',
            'address_city',
            'address_street',
            'address_house',
            'address_appartment'
        )

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():

            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.patronim_name = validated_data['patronim_name']
        instance.email = validated_data['email']
        instance.birth_date = validated_data['birth_date']
        instance.phone_num = validated_data['phone_num']
        instance.address_city = validated_data['address_city']
        instance.address_street = validated_data['address_street']
        instance.address_house = validated_data['address_house']
        instance.address_appartment = validated_data['address_appartment']

        instance.save()

        return instance
