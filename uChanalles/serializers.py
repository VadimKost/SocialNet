from django.contrib.auth.models import User
from rest_framework import serializers
from chat.models import User_M

class UserSerializer(serializers.ModelSerializer):
    chats=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'last_login', 'date_joined', 'is_staff', 'is_active']


class User_detail_Serializer(serializers.ModelSerializer):
    img=serializers.CharField(source='img_url')
    user=UserSerializer()
    class Meta:
        model = User_M
        fields = '__all__'
        depth = 1


