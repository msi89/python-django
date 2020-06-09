from rest_framework import serializers
from account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'full_name', 'email', 'username',
                  'is_admin', 'is_active', 'date_joined', 'last_login']


class UpdateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'full_name', 'email', 'username', 'is_admin',
                  'is_active', 'date_joined', 'last_login']
        extra_kwargs = {
            'email': {'read_only': True},
            'username': {'read_only': True},
        }


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['full_name', 'email', 'username',
                  'password',  'is_admin', 'is_active', 'date_joined', 'last_login']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'read_only': True},
            'full_name': {'read_only': True},
        }


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['full_name', 'email', 'username',
                  'password', 'password2', 'is_admin', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            full_name=self.validated_data['full_name'],
            is_admin=self.validated_data['is_admin'],
            is_active=self.validated_data['is_active'],
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account
