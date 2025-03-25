from django.urls import include
from rest_framework import routers
from rest_framework import viewsets
from rest_framework import serializers
from . import models

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = '__all__'

class AccountViewSet(viewsets.ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = AccountSerializer

router = routers.DefaultRouter()
router.register(r'', AccountViewSet, basename='accounts')

urlpatterns =router.urls
