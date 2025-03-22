import pytest

from billboard import AlbumChart, ArtistChart, SongCharts


@pytest.fixture(scope="session")
def songs():
    songs = SongCharts("2024-08-08")
    return songs


@pytest.fixture
def hot_chart(songs):
    return songs.hot100


@pytest.fixture
def glob_chart(songs):
    return songs.global200


@pytest.fixture(scope="session")
def artist_chart():
    artist = ArtistChart("2024-08-08", auto_gen=True)
    return artist


@pytest.fixture(scope="session")
def album_chart():
    album = AlbumChart("2024-08-08", auto_gen=True)
    return album
