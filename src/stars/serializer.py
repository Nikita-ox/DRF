from rest_framework import serializers

from stars.models import Stars


class StarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stars
        fields = ('title', 'cat_id')
