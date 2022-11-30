import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.serializers import ModelSerializer

from stars.models import Stars


# class StarsModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class StarsSerializer(ModelSerializer):
    class Meta:
        model = Stars
        fields = "__all__"














