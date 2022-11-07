from rest_framework import serializers
from library.models import *


class ArtistSerializer(serializers.ModelSerializer):
    """
    Сериализация модели исполнителя
    """

    class Meta:
        model = Artist
        fields = ('id', 'title')
        read_only_fields = ('id',)


class SongSerializer(serializers.ModelSerializer):
    """
    Сериализация модели песни
    """

    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Song
        fields = ('id', 'title', 'duration', 'artist')
        read_only_fields = ('id',)


class AlbumSerializer(serializers.ModelSerializer):
    """
    Сериализация модели альбома
    """

    songs = SongSerializer(read_only=True, many=True)

    class Meta:
        model = Album
        fields = ('id', 'title', 'release_date', 'songs')
        read_only_fields = ('id',)
