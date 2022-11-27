from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from stars.models import Stars
from stars.serializers import StarsSerializer


class StarsAPIView(APIView):
    def get(self, request):
        s = Stars.objects.all()
        return Response({'posts': StarsSerializer(s, many=True).data})

    def post(self, request):
        serializers = StarsSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)

        post_new = Stars.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': StarsSerializer(post_new).data})


# class StarsAPIView(generics.ListAPIView):
#     queryset = Stars.objects.all()
#     serializer_class = StarsSerializer
