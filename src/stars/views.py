from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from rest_framework import generics, mixins
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from stars.models import Stars
from stars.serializers import StarsSerializer

'''

'''
class StarsViewSet(ModelViewSet):
    queryset = Stars.objects.all()
    serializer_class = StarsSerializer



