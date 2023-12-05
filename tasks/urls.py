from django.urls import path
from tasks import views

urlpatterns = [
    # Task Operations [List, Create, Retreive, Update, Delete]
    path("", views.ListCreateTask.as_view()),
    path("<int:pk>/", views.RetrieveUpdateDestroyTask.as_view()),
]
