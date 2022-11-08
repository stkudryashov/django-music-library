from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from drf_spectacular.utils import extend_schema_view, extend_schema

from library.serializers import *
from library.models import *


@extend_schema_view(
    list=extend_schema(description='Получить список исполнителей'),
    create=extend_schema(description='Создать нового исполнителя'),
    retrieve=extend_schema(description='Получить исполнителя по id'),
    update=extend_schema(description='Заменить исполнителя'),
    partial_update=extend_schema(description='Редактировать исполнителя'),
    destroy=extend_schema(description='Удалить исполнителя'),
)
class ArtistViewSet(ModelViewSet):
    """
    Создание и получение исполнителей
    """

    permission_classes = [AllowAny]

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


@extend_schema_view(
    list=extend_schema(description='Получить список песен'),
    create=extend_schema(description='Создать новую песню'),
    retrieve=extend_schema(description='Получить песню по id'),
    update=extend_schema(description='Заменить песню'),
    partial_update=extend_schema(description='Редактировать песню'),
    destroy=extend_schema(description='Удалить песню'),
)
class SongViewSet(ModelViewSet):
    """
    Создание и получение песен
    """

    permission_classes = [AllowAny]

    queryset = Song.objects.all()
    serializer_class = SongSerializer


@extend_schema_view(
    list=extend_schema(description='Получить список альбомов'),
    create=extend_schema(description='Создать новый альбом'),
    retrieve=extend_schema(description='Получить альбом по id'),
    update=extend_schema(description='Заменить альбом'),
    partial_update=extend_schema(description='Редактировать альбом'),
    destroy=extend_schema(description='Удалить альбом'),
)
class AlbumViewSet(ModelViewSet):
    """
    Создание и получение альбомов
    """

    permission_classes = [AllowAny]

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
