import pytest

from billboard import AlbumChart, ArtistChart, SongCharts


@pytest.fixture(scope="session")
def songs():
    return SongCharts("2024-08-08")


@pytest.fixture
def hot_chart(songs):
    return songs.hot100


@pytest.fixture
def glob_chart(songs):
    return songs.global200


@pytest.fixture(scope="session")
def artist_chart():
    return ArtistChart("2024-08-08")


@pytest.fixture(scope="session")
def album_chart():
    return AlbumChart("2024-08-08")
