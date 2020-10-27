from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from userprofile.models import ContactAndLinks
from userprofile.serializers import UserSerializer, ContactAndLinksSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ContactAndLinksViewSet(viewsets.ModelViewSet):
    serializer_class = ContactAndLinksSerializer

    def get_queryset(self):
        user=self.request.user
        return ContactAndLinks.objects.filter(user=user)
