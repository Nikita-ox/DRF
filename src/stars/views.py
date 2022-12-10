from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView

from rest_framework.response import Response
from rest_framework.views import APIView

from stars.models import Stars
from stars.serializers import StarsSerializer


def start(request):
    return HttpResponse("<h1>Главная страница</h1>")



class StarsAPIList(ListCreateAPIView):
    queryset = Stars.objects.all()
    serializer_class = StarsSerializer





