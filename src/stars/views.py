from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from stars.models import Stars
from stars.serializer import StarsSerializer


class StarsAPIView(APIView):
    def get(self, request):
        lst = Stars.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = Stars.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})


# class StarsAPIView(generics.ListAPIView):
#     queryset = Stars.objects.all()
#     serializer_class = StarsSerializer
