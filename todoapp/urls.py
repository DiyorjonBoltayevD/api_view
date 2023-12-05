from django.urls import path

from todoapp.views import *

urlpatterns = [
    path('tasks/', HomeApiView.as_view()),
    path('tasks/create/', TaskCreateApiView.as_view()),
    path('tasks/listcreate/', TaskListCreateApiView.as_view()),
    path('tasks/update/<int:pk>/', TaskUpdateApiView.as_view()),
    path('tasks/delete/<int:pk>/', TaskDestroyApiView.as_view()),
    path('tasks/<int:pk>/', TaskDetailApiView.as_view()),
    path('tasks/detail/update/<int:pk>/', TaskDetailUpdateApiView.as_view()),
    path('tasks/detail/delete/<int:pk>/', TaskDetailDeleteApiView.as_view()),
    path('tasks/detail/all/<int:pk>/',TaskDetailALLApiView.as_view())

]
