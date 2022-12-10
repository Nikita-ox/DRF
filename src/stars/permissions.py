from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
            return True
        # def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение на уровне объекта, позволяющее редактировать его только владельцам объекта.
    Предполагается, что экземпляр модели имеет атрибут 'user'.
    """

    def has_object_permission(self, request, view, obj):
        """
        Разрешения на чтение разрешены для любого запроса,
        поэтому мы всегда будем разрешать запросы GET, HEAD или OPTIONS
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        """Экземпляр должен иметь атрибут с именем 'user'"""
        """
        user из базы данных равен user, который пришёл с запросом даём доступ
        """
        return obj.user == request.user


