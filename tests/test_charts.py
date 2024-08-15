from datetime import datetime

import pytest
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

    def test_date_exception(self):
        with pytest.raises(ValueError) as _:
            _ = BillboardChart("01/01/24")
