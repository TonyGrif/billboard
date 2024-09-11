import pytest

from billboard import SongCharts


@pytest.fixture(scope="session")
def songs():
    return SongCharts("2024-08-08")


@pytest.fixture
def hot_chart(songs):
    return songs.hot100


@pytest.fixture
def glob_chart(songs):
    return songs.global200
