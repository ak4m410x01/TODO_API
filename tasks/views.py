from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from tasks.models import Task
from tasks.serializers import TaskSerializer, UserSerializer
from tasks.permissions import IsTaskOwner, IsUserDetails

# Create your views here.


class ListTask(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsTaskOwner]
    metadata_class = ("GET",)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreateTask(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]
    metadata_class = ("POST",)


class RetrieveUpdateDestroyTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsTaskOwner]


class ListCreateUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

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


@permission_classes([IsAuthenticated, IsUserDetails])
class RegenrateUserToken(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            response = {"token": "must be logged in"}
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)

        token = Token.objects.get(user=request.user.id)
        response = {
            "token": token.key,
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            response = {"token": "must be logged in"}
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)

        user = self.request.user
        Token.objects.filter(user=user.id).delete()
        token = Token.objects.create(user=user)
        response = {
            "token": token.key,
        }
        return Response(response, status=status.HTTP_201_CREATED)
