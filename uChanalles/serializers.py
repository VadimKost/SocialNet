from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import User_M, Chat, Message, User_photo


# Serializer
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_photo
        fields='__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'id', ]


class User_M_Serializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(source='get_user_name')
    email = serializers.CharField(source='get_email')
    img = serializers.CharField(source='img_url')
    class Meta:
        model = User_M
        fields = ['user', 'username', 'email', 'adress', 'phone', 'AboutMe', 'url','img']


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ['autor', 'message']


class ChatSerializer(serializers.HyperlinkedModelSerializer):
    messeges = MessageSerializer(many=True)

    class Meta:
        model = Chat
        fields = ['url', 'id', 'name', 'messeges', 'members']


# ViewSet
@permission_classes([IsAuthenticated, ])
class User_M_ViewSet(viewsets.ModelViewSet):
    queryset = User_M.objects.all()
    serializer_class = User_M_Serializer


# ViewSets define the view behavior.
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, ])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@permission_classes([IsAuthenticated, ])
class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


@permission_classes([IsAuthenticated, ])
class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


@permission_classes([IsAuthenticated, ])
class CurrentUser(APIView):
    def get(self, request):
        serializer_context = {
            'request': request,
        }
        qs=User_M.objects.get(user=request.user)
        serializer=User_M_Serializer(qs,context=serializer_context)
        return Response(serializer.data)
