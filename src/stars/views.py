from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

from stars.models import Stars
from stars.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from stars.serializers import StarsSerializer


class StarsAPIList(ListCreateAPIView):
    queryset = Stars.objects.all()
    serializer_class = StarsSerializer
    """
    Изменение данных только зарегестрированным пользователям
    иначе просто чтение
    """
    permission_classes = [IsAuthenticatedOrReadOnly]


class StarsAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Stars.objects.all()
    serializer_class = StarsSerializer
    permission_classes = (IsAuthenticated,)  # Поменяли IsOwnerOrReadOnly
    # authentication_classes = (TokenAuthentication,)  # Доступ только по токену
    """Запятая после означает кортеж"""


class StarsAPIDestroy(RetrieveDestroyAPIView):
    queryset = Stars.objects.all()
    serializer_class = StarsSerializer
    """
    Удалять может только администратор,
    а читать все пользователи
    """
    permission_classes = (IsAdminOrReadOnly,)
