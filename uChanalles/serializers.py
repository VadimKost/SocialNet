from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer