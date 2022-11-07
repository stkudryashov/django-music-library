from django.contrib import admin
from library.models import *


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

    search_fields = ('title',)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'duration', 'artist')
    list_display_links = ('id', 'title')

    search_fields = ('title',)


class AlbumSongInline(admin.TabularInline):
    model = AlbumSong
    extra = 1

    verbose_name_plural = 'Список песен'


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date')
    list_display_links = ('id', 'title')

    search_fields = ('title',)
    inlines = (AlbumSongInline,)


@admin.register(AlbumSong)
class AlbumSongAdmin(admin.ModelAdmin):
    list_display = ('id', 'album', 'song', 'order')
