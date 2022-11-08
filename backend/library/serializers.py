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

    artist = ArtistSerializer(read_only=True)
    artist_id = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all(), source='artist', write_only=True)

    class Meta:
        model = Song
        fields = ('id', 'title', 'duration', 'artist', 'artist_id')
        read_only_fields = ('id',)


class AlbumSongSerializer(serializers.ModelSerializer):
    """
    Сериализация песен и их порядка в альбоме
    """

    song_id = serializers.PrimaryKeyRelatedField(queryset=Song.objects.all(), source='song')

    class Meta:
        model = AlbumSong
        fields = ('id', 'song_id', 'order')
        read_only_fields = ('id',)


class AlbumSerializer(serializers.ModelSerializer):
    """
    Сериализация модели альбома
    """

    track_list = SerializerMethodField(method_name='get_order_songs_list')
    songs = AlbumSongSerializer(many=True, write_only=True)

    class Meta:
        model = Album
        fields = ('id', 'title', 'release_date', 'track_list', 'songs')
        read_only_fields = ('id', 'track_list')

    def get_order_songs_list(self, instance):
        track_list = instance.songs.order_by('albumsong__order')
        return SongSerializer(track_list, many=True, read_only=True).data

    def create(self, validated_data):
        album_songs = validated_data.pop('songs')
        album = Album.objects.create(**validated_data)

        for song in album_songs:
            AlbumSong.objects.create(album=album, song=song.get('song'), order=song.get('order'))
        return album
