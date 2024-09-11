from datetime import datetime, timedelta

import pytest
from hamcrest import any_of, assert_that, equal_to, has_length

from billboard import GlobalChart


@pytest.fixture(scope="module")
def chart():
    return GlobalChart("2024-08-08")


class TestGlobalChart:
    def test_init(self, chart):
        assert_that(chart.date, equal_to("2024-08-08"))
        assert_that(chart.chart, has_length(200))

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

    def test_top_spot(self, chart):
        top = chart.top_spot
        assert_that(top.rank, equal_to(1))
        assert_that(top.title, equal_to("Who"))
        assert_that(top.artist, equal_to("Jimin"))
        assert_that(top.last_week_rank, equal_to("1"))
        assert_that(top.peak_rank, equal_to("1"))
        assert_that(top.weeks_on_chart, equal_to("2"))

    def test_get_artist(self, chart):
        artist = chart.artist_entries("Chappell Roan", 200)
        assert_that(artist, has_length(4))

        artist = chart.artist_entries("chappell roan", 200)
        assert_that(artist, has_length(4))

        artist = chart.artist_entries("Chappell Roan", rank=50)
        assert_that(artist, has_length(2))
