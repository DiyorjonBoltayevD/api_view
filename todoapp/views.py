from django.shortcuts import render

from .models import *
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, \
    RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TodoSerializer


class HomeApiView(ListAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer


class TaskCreateApiView(CreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer


class TaskUpdateApiView(UpdateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer


class TaskDestroyApiView(DestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer


class TaskListCreateApiView(ListCreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer


class TaskDetailApiView(RetrieveAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer


class TaskDetailUpdateApiView(RetrieveUpdateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer


class TaskDetailDeleteApiView(RetrieveDestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer


class TaskDetailALLApiView(RetrieveUpdateDestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
