import pytest
from datetime import datetime
from hamcrest import assert_that, equal_to
from billboard import BillboardChart


@pytest.fixture
def chart():
    return BillboardChart("2024-01-01")


class TestBillboardChart:
    def test_init(self, chart):
        assert_that(chart.date, equal_to("2024-01-01"))

        cur = BillboardChart()
        assert_that(cur.date, equal_to(datetime.today().strftime("%Y-%m-%d")))
