from django.db import models


class Artist(models.Model):
    title = models.CharField(max_length=128, verbose_name='Исполнитель')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Song(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    duration = models.IntegerField(verbose_name='Длительность (сек.)')

    artist = models.ForeignKey(Artist, related_name='songs', on_delete=models.PROTECT, verbose_name='Исполнитель')

    def __str__(self):
        return f'{self.artist.title} - {self.title}'

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'


class Album(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    release_date = models.DateField(verbose_name='Дата релиза')

    songs = models.ManyToManyField(Song, through='AlbumSong', verbose_name='Песни')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


class AlbumSong(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='Альбом')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name='Песня')

    order = models.PositiveIntegerField(verbose_name='Порядок песни в альбоме')

    def __str__(self):
        return f'{self.album.title} - {self.song.title}'

    class Meta:
        verbose_name = 'Песни в альбоме'
        verbose_name_plural = 'Песни в альбомах'

        # ordering = ('order', )

        constraints = [
            models.UniqueConstraint(fields=['album', 'song'], name='unique_album_song'),
        ]
