from django.urls import path, include
from users import views

urlpatterns = [
    path("", include("auths.urls")),
    path("", views.ListCreateUser.as_view()),
    path("<int:pk>/", views.RetrieveUpdateDestroyUser.as_view()),
]
