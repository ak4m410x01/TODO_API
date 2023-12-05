from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes

from users.permissions import IsUserDetails


@permission_classes([IsAuthenticated, IsUserDetails])
class RegenerateUserToken(APIView):
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
