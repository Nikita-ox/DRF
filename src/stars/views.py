from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from rest_framework import generics, mixins
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from stars.models import Stars, Category
from stars.serializers import StarsSerializer


class StarsViewSet(ModelViewSet):
    # queryset = Stars.objects.all()
    serializer_class = StarsSerializer
    '''
    Вернуть клиенту, по определённому адресу
    ограниченное кол-во записей
    '''

    def get_queryset(self):  # Всегда возвращает список
        """
        Получаем ключ pk
        """
        pk = self.kwargs.get("pk")

        if not pk:
            return Stars.objects.all()[:3]

        return Stars.objects.filter(pk=pk)
    '''
    filter возвращает список, но из одной записи
    '''

    '''
    Что бы выбрать конкретную категорию по pk
    '''

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        category = Category.objects.get(pk=pk)

        return Response({'категории': category.name})

    '''
    Путь с указанием конкретного pk  
    http://127.0.0.1:8000/api/v1/stars/1/category/
    pk прописывается перед 'category'
    '''
