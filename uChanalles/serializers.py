from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, permissions, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from chat.models import User_M, Chat, Message, User_photo

# class IsOwnerOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD or OPTIONS requests.
#         if request.method in permissions.SAFE_METHODS:
#             return True
#
#         # Instance must have an attribute named `owner`.
#         return obj.user == request.user
#
# # Serializer
# class PhotoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User_photo
#         fields='__all__'
#
#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff', 'id','password' ]
#
#
# class User_M_Serializer(serializers.HyperlinkedModelSerializer):
#     username = serializers.CharField(source='get_user_name')
#     email = serializers.CharField(source='get_email')
#     img = serializers.CharField(source='img.photo.url')
#     class Meta:
#         model = User_M
#         fields = ['user', 'username', 'email', 'adress', 'phone', 'AboutMe', 'url','img']
#
#
# class MessageSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Message
#         fields = ['autor', 'message']
#
#
# class ChatSerializer(serializers.HyperlinkedModelSerializer):
#     messeges = MessageSerializer(many=True)
#
#     class Meta:
#         model = Chat
#         fields = ['url', 'id', 'name', 'messeges', 'members']
#
#
# # ViewSet
# @permission_classes([IsAuthenticated,IsOwnerOrReadOnly])
# class User_M_ViewSet(viewsets.ModelViewSet):
#     queryset = User_M.objects.all()
#     serializer_class = User_M_Serializer
#
#
# # ViewSets define the view behavior.
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated,IsOwnerOrReadOnly ])
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# @permission_classes([IsAuthenticated, ])
# class ChatViewSet(viewsets.ModelViewSet):
#     queryset = Chat.objects.all()
#     serializer_class = ChatSerializer
#
#
# @permission_classes([IsAuthenticated, ])
# class MessagesViewSet(viewsets.ModelViewSet):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#
#
# @permission_classes([IsAuthenticated, ])
# class CurrentUser(APIView):
#     def get(self, request):
#         serializer_context = {
#             'request': request,
#         }
#         qs=User_M.objects.get(user=request.user)
#         serializer=User_M_Serializer(qs,context=serializer_context)
#         return Response(serializer.data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = '__all__'

class UserView(APIView):
    def get(self,request):
        qs=User.objects.all()
        serializer=UserSerializer(qs,many=True)
        return Response(serializer.data)


class User_detail_Serializer(serializers.ModelSerializer):
    class Meta:
        model=User_M
        fields = '__all__'
        depth=1


class User_detail_View(APIView):
    def get(self,request):
        qs=User_M.objects.all()
        serializer=User_detail_Serializer(qs,many=True)
        return Response(serializer.data)


class CurrentUserView(APIView):
    def get(self, request):
        serializer_context = {
            'request': request,
        }
        qs=User_M.objects.get(user=request.user)
        serializer=User_detail_Serializer(qs,context=serializer_context)
        return Response(serializer.data)
