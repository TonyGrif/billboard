from datetime import datetime, timedelta

import pytest
from hamcrest import any_of, assert_that, equal_to, has_length

from billboard import BillboardChart


@pytest.fixture
def chart():
    return BillboardChart("2024-08-08")


class TestBillboardChart:
    def test_init(self, chart):
        assert_that(chart.date, equal_to("2024-08-08"))
        assert_that(chart.chart, has_length(100))

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

    def test_data(self, chart):
        assert_that(chart.top_spot.rank, equal_to("1"))
        assert_that(chart.top_spot.title, equal_to("A Bar Song (Tipsy)"))
        assert_that(chart.top_spot.artist, equal_to("Shaboozey"))
        assert_that(chart.top_spot.last_week_rank, equal_to("1"))
        assert_that(chart.top_spot.peak_rank, equal_to("1"))
        assert_that(chart.top_spot.weeks_on_chart, equal_to("16"))
