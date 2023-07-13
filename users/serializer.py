from rest_framework.serializers import ModelSerializer, CharField, ValidationError

from users.models import User


class RegisterSerializer(ModelSerializer):
    password = CharField(max_length=60, min_length=6, write_only=True)
    password2 = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password', '')
        password2 = attrs.get('password2', '')

        if password != password2:
            raise ValidationError(
                'The two password fields didn\'t match.'
            )
        return attrs

    def create(self, validated_data: dict):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)
