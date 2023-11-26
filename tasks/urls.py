from django.urls import path
from tasks import views

urlpatterns = [
    # Token Operations [Retreive, Regenerate]
    path("token/", views.RegenrateUserToken.as_view()),
    # Task Operations [List, Create, Retreive, Update, Delete]
    path("tasks/", views.ListTask.as_view()),
    path("tasks/create", views.CreateTask.as_view()),
    path("tasks/<int:pk>/", views.RetrieveUpdateDestroyTask.as_view()),
    # User Operations [List, Create, Retreive, Update, Delete]
    path("users/", views.ListCreateUser.as_view()),
    path("users/<int:pk>/", views.RetrieveUpdateDestroyUser.as_view()),
]
