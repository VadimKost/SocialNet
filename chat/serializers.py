from django.contrib.auth.models import User
from rest_framework import serializers
from chat.models import User_M,User_photo


class Main_imgSerializer(serializers.ModelSerializer):
    class Meta:
        model=User_photo
        fields = '__all__'

class User_detail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_M
        exclude=['user']
        depth = 1

class UserSerializer(serializers.ModelSerializer):
    chats=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    img=Main_imgSerializer(required=False)
    user_i=User_detail_Serializer(required=False)
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'last_login', 'date_joined', 'is_staff', 'is_active']
        depth = 1





