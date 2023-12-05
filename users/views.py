from django.contrib.auth.models import User

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from users.serializers import UserSerializer
from users.permissions import IsUserDetails


class ListCreateUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()

    def list(self, request, *args, **kwargs):
        response = {
            "error": "operation not allowed",
        }
        return Response(response, status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        token = Token.objects.get(user=serializer.instance)
        headers = self.get_success_headers(serializer.data)

        response = {
            "token": token.key,
        }
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)


class RetrieveUpdateDestroyUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUserDetails]
