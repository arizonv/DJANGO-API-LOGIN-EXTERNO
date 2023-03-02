from rest_framework import status
from .serializers import UserSerializer
from rest_framework import serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import authentication, permissions

class LoginView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data)
        else:
            return Response({"error": "Invalid credentials"}, status=400)


class UserLogout(APIView):
    def get(self, request):
        logout(request)
        return Response('User Logged out successfully')

# class LoginView(APIView):
#     authentication_classes = (BasicAuthentication)
#     permission_classes = (IsAuthenticated)

#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         user = authenticate(username=username, password=password)
#         print(user)
#         if user is not None:
#             user_serializer = UserSerializer(user)
#             return Response({"message": "Login successful", "user": user_serializer.data})
#         else:
#             return Response({"error": "Invalid credentials"},
#                             status=status.HTTP_400_BAD_REQUEST)



