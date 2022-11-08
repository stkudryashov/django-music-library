from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from drf_spectacular.utils import extend_schema_view, extend_schema

from library.serializers import *
from library.models import *


@extend_schema_view(
    list=extend_schema(description='Получить список исполнителей', tags=['Artists']),
    create=extend_schema(description='Создать нового исполнителя', tags=['Artists']),
    retrieve=extend_schema(description='Получить исполнителя по id', tags=['Artists']),
    update=extend_schema(description='Заменить исполнителя', tags=['Artists']),
    partial_update=extend_schema(description='Редактировать исполнителя', tags=['Artists']),
    destroy=extend_schema(description='Удалить исполнителя', tags=['Artists']),
)
class ArtistViewSet(ModelViewSet):
    """
    Создание и получение исполнителей
    """

    permission_classes = [AllowAny]

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


@extend_schema_view(
    list=extend_schema(description='Получить список песен', tags=['Songs']),
    create=extend_schema(description='Создать новую песню', tags=['Songs']),
    retrieve=extend_schema(description='Получить песню по id', tags=['Songs']),
    update=extend_schema(description='Заменить песню', tags=['Songs']),
    partial_update=extend_schema(description='Редактировать песню', tags=['Songs']),
    destroy=extend_schema(description='Удалить песню', tags=['Songs']),
)
class SongViewSet(ModelViewSet):
    """
    Создание и получение песен
    """

    permission_classes = [AllowAny]

    queryset = Song.objects.all()
    serializer_class = SongSerializer


@extend_schema_view(
    list=extend_schema(description='Получить список альбомов', tags=['Albums']),
    create=extend_schema(description='Создать новый альбом', tags=['Albums']),
    retrieve=extend_schema(description='Получить альбом по id', tags=['Albums']),
    update=extend_schema(description='Заменить альбом', tags=['Albums']),
    partial_update=extend_schema(description='Редактировать альбом', tags=['Albums']),
    destroy=extend_schema(description='Удалить альбом', tags=['Albums']),
)
class AlbumViewSet(ModelViewSet):
    """
    Создание и получение альбомов
    """

    permission_classes = [AllowAny]

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
