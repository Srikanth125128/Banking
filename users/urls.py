

from django.urls import include
from rest_framework import routers
from rest_framework import viewsets
from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'', UserViewSet, basename='users')

urlpatterns = router.urls



