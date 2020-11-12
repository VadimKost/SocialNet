from django.contrib.auth.models import User
from rest_framework import serializers

from userprofile.models import UserProfile, ContactAndLinks


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude=['user']

class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()

    def create(self, validated_data):
        userProfile=validated_data.pop('user_profile')
        user=User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        UserProfile.objects.create(user=user,**userProfile)
        return user


    class Meta:
        model = User
        exclude = [ 'is_superuser', 'last_login', 'date_joined', 'is_staff', 'is_active','groups','user_permissions']
        extra_kwargs = {'password': {'write_only': True}}

class ContactAndLinksSerializer(serializers.ModelSerializer):

    class Meta:
        model= ContactAndLinks
        fields='__all__'