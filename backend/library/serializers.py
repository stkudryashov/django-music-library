from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

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

    artist = ArtistSerializer()

    class Meta:
        model = Song
        fields = ('id', 'title', 'duration', 'artist')
        read_only_fields = ('id',)


class AlbumSerializer(serializers.ModelSerializer):
    """
    Сериализация модели альбома
    """

    songs = SerializerMethodField(method_name='get_order_songs_list')

    class Meta:
        model = Album
        fields = ('id', 'title', 'release_date', 'songs')
        read_only_fields = ('id',)

    def get_order_songs_list(self, instance):
        songs = instance.songs.order_by('albumsong__order')
        return SongSerializer(songs, many=True).data
