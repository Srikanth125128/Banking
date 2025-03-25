from rest_framework import serializers
from .models import Account
from users.serializers import UserSerializer

class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Account
        fields = ['id', 'user', 'account_number', 'balance']
