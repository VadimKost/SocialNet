from django.contrib.auth.models import User
from rest_framework import serializers

from chat.models import User_photo, User_M


class Main_imgSerializer(serializers.ModelSerializer):
    class Meta:
        model=User_photo
        exclude=['user']

class User_iSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_M
        exclude=['user']

class UserSerializer(serializers.ModelSerializer):
    img = Main_imgSerializer()
    user_i = User_iSerializer(required=False)

    def create(self, validated_data):
        user_i=validated_data.pop('user_i')
        img=validated_data.pop('img')
        user=User.objects.create(**validated_data)
        User_M.objects.create(user=user,**user_i)
        User_photo.objects.create(user=user,**img)
        return user


    class Meta:
        model = User
        exclude = [ 'is_superuser', 'last_login', 'date_joined', 'is_staff', 'is_active','groups','user_permissions']
        extra_kwargs = {'password': {'write_only': True}}
