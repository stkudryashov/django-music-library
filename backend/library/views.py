from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from library.serializers import *
from library.models import *


class ArtistViewSet(ModelViewSet):
    """
    Создание и получение исполнителей
    """

    permission_classes = [AllowAny]

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class SongViewSet(ModelViewSet):
    """
    Создание и получение песен
    """

    permission_classes = [AllowAny]

    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AlbumViewSet(ModelViewSet):
    """
    Создание и получение альбомов
    """

    permission_classes = [AllowAny]

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
