from rest_framework.viewsets import ModelViewSet

from library.serializers import *
from library.models import *


class ArtistViewSet(ModelViewSet):
    """
    Создание и получение исполнителей
    """

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class SongViewSet(ModelViewSet):
    """
    Создание и получение песен
    """

    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AlbumViewSet(ModelViewSet):
    """
    Создание и получение альбомов
    """

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
