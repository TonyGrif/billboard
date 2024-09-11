from datetime import datetime, timedelta

import pytest
from hamcrest import any_of, assert_that, equal_to, has_length

from billboard import BillboardChart, GlobalChart, SongCharts


@pytest.fixture(scope="session")
def charts():
    return SongCharts("2024-08-08")


@pytest.fixture
def hot_chart(charts):
    return charts.hot100


@pytest.fixture
def glob_chart(charts):
    return charts.global200


class TestBillboardChart:
    def test_init(self, hot_chart):
        assert_that(hot_chart.date, equal_to("2024-08-08"))
        assert_that(hot_chart.chart, has_length(100))

        cur = BillboardChart(auto_date=False)
        yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        assert_that(cur.date, equal_to(yesterday))
        assert_that(len(cur.chart), any_of(equal_to(0), equal_to(100)))

    def test_date_exception(self):
        with pytest.raises(ValueError) as _:
            _ = BillboardChart("01/01/24")

        with pytest.raises(ValueError) as _:
            _ = BillboardChart("1958-07-04")

        with pytest.raises(ValueError) as _:
            not_yet = datetime.today() + timedelta(weeks=1)
            _ = BillboardChart(not_yet.strftime("%Y-%m-%d"))

    def test_top_spot(self, hot_chart):
        top = hot_chart.top_spot
        assert_that(top.rank, equal_to(1))
        assert_that(top.title, equal_to("A Bar Song (Tipsy)"))
        assert_that(top.artist, equal_to("Shaboozey"))
        assert_that(top.last_week_rank, equal_to("1"))
        assert_that(top.peak_rank, equal_to("1"))
        assert_that(top.weeks_on_chart, equal_to("16"))

    def test_get_artist(self, hot_chart):
        artist = hot_chart.artist_entries("Chappell Roan")
        assert_that(artist, has_length(6))

        artist = hot_chart.artist_entries("chappell roan")
        assert_that(artist, has_length(6))

        artist = hot_chart.artist_entries("Chappell Roan", rank=50)
        assert_that(artist, has_length(3))


class TestGlobalChart:
    def test_init(self, glob_chart):
        assert_that(glob_chart.date, equal_to("2024-08-08"))
        assert_that(glob_chart.chart, has_length(200))

        cur = GlobalChart(auto_date=False)
        yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        assert_that(cur.date, equal_to(yesterday))
        assert_that(len(cur.chart), any_of(equal_to(0), equal_to(200)))

    def test_date_exception(self):
        with pytest.raises(ValueError) as _:
            _ = GlobalChart("01/01/24")

        with pytest.raises(ValueError) as _:
            _ = GlobalChart("2020-09-01")

        with pytest.raises(ValueError) as _:
            not_yet = datetime.today() + timedelta(weeks=1)
            _ = GlobalChart(not_yet.strftime("%Y-%m-%d"))

    def test_top_spot(self, glob_chart):
        top = glob_chart.top_spot
        assert_that(top.rank, equal_to(1))
        assert_that(top.title, equal_to("Who"))
        assert_that(top.artist, equal_to("Jimin"))
        assert_that(top.last_week_rank, equal_to("1"))
        assert_that(top.peak_rank, equal_to("1"))
        assert_that(top.weeks_on_chart, equal_to("2"))

    def test_get_artist(self, glob_chart):
        artist = glob_chart.artist_entries("Chappell Roan", 200)
        assert_that(artist, has_length(4))

        artist = glob_chart.artist_entries("chappell roan", 200)
        assert_that(artist, has_length(4))

        artist = glob_chart.artist_entries("Chappell Roan", rank=50)
        assert_that(artist, has_length(2))
