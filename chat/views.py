
# def room(request, room_id):
#     x1=datetime.now()
#     room_name_json=mark_safe(json.dumps(room_id))
#     try:
#         messages=Message.objects.filter(chat=room_id)
#
#     except:
#         error="Wrire"
#         messages.delete()
#     x2=datetime.now()
#     print(x2-x1)
#     return render(request, 'room.html',locals())
#
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import User_M
from chat.serializers import User_detail_Serializer, UserSerializer


class UserView(APIView):
    """Standart user model api """
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            to_return = User.objects.create_user(
                email=serializer.initial_data['email'],
                username=serializer.initial_data['username'],
                password=serializer.initial_data['password']
            )
            return Response(UserSerializer(to_return).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        qs = User.objects.all()
        serializer = UserSerializer(qs, many=True)
        return Response(serializer.data)


class User_detail_View(APIView):
    """Extended user model api"""
    def post(self, request):
        serializer = User_detail_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

    def get(self, request):
        qs = User_M.objects.all()
        serializer = User_detail_Serializer(qs, many=True)
        return Response(serializer.data)


class CurrentUserView(APIView):
    """Current user detail inf api"""
    def get(self, request):
        serializer_context = {
            'request': request,
        }
        qs = User.objects.get(id=request.user.id)
        serializer = UserSerializer(qs, context=serializer_context)
        return Response(serializer.data)
