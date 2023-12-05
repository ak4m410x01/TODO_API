from django.urls import path
from auths.views import RegenerateUserToken

urlpatterns = [
    path("token/", RegenerateUserToken.as_view()),
]
