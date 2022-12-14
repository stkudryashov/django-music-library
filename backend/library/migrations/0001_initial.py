# Generated by Django 4.1.3 on 2022-11-07 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('release_date', models.DateField(verbose_name='Дата релиза')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Исполнитель')),
            ],
            options={
                'verbose_name': 'Исполнитель',
                'verbose_name_plural': 'Исполнители',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('duration', models.IntegerField(verbose_name='Длительность (сек.)')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='songs', to='library.artist', verbose_name='Исполнитель')),
            ],
            options={
                'verbose_name': 'Песня',
                'verbose_name_plural': 'Песни',
            },
        ),
        migrations.CreateModel(
            name='AlbumSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(verbose_name='Порядок песни в альбоме')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.album', verbose_name='Альбом')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.song', verbose_name='Песня')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='songs',
            field=models.ManyToManyField(through='library.AlbumSong', to='library.song', verbose_name='Песни'),
        ),
        migrations.AddConstraint(
            model_name='albumsong',
            constraint=models.UniqueConstraint(fields=('album', 'song'), name='unique_album_song'),
        ),
    ]
