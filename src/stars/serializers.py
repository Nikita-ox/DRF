import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from stars.models import Stars


# class StarsModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class StarsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=2000)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()  # ForeignKey перобразовывается

# def encode():
#     model = StarsModel('Angelina Jolie', 'Kristian Stuart')
#     model_sr = StarsSerializer(model)
#     print(model_sr.data, sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Kristian Stuart"}')
#     data = JSONParser().parse(stream)
#     serializers = StarsSerializer(data=data)
#     serializers.is_valid()
#     print(serializers.validated_data)
