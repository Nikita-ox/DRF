from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from stars.models import Stars


class StarsSerializer(ModelSerializer):
    """Связь с моделью Stars, с полем user"""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    """
    HiddenField - скрытое поле и по умолчанию  default
    прописывается текущий пользователь CurrentUserDefault
    """

    class Meta:
        model = Stars
        fields = "__all__"

