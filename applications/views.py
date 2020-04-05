from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ApplicationSerializer
from .models import Application
# Create your views here.


#


class ApplicationView(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer