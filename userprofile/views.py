from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


from userprofile.models import ContactAndLinks
from userprofile.serializers import UserSerializer, ContactAndLinksSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False)
    def currentUser(self,request):
        if self.request.user.id == None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(UserSerializer(self.request.user).data,status=status.HTTP_200_OK)

class ContactAndLinksViewSet(viewsets.ModelViewSet):
    serializer_class = ContactAndLinksSerializer

    def get_queryset(self):
        user=self.request.user
        return ContactAndLinks.objects.filter(user=user)
