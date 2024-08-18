import pytest
from hamcrest import assert_that, contains_string, equal_to, has_length

from billboard.utils import make_request, parse_request


@pytest.fixture
def response():
    return make_request("2024-08-15")


def test_make_request(response):
    assert_that(response.text, contains_string("360"))
    assert_that(response.text, contains_string("Charli xcx"))


def test_parse_request(response):
    chart = parse_request(response)
    assert_that(chart, has_length(100))

    top = chart[0]
    assert_that(top.rank, equal_to("1"))
    assert_that(top.title, equal_to("A Bar Song (Tipsy)"))
    assert_that(top.artist, equal_to("Shaboozey"))
    assert_that(top.last_week_rank, equal_to("1"))
    assert_that(top.peak_rank, equal_to("1"))
    assert_that(top.weeks_on_chart, equal_to("17"))

    varied = chart[3]
    assert_that(varied.rank, equal_to("4"))
    assert_that(varied.title, equal_to("Espresso"))
    assert_that(varied.artist, equal_to("Sabrina Carpenter"))
    assert_that(varied.last_week_rank, equal_to("4"))
    assert_that(varied.peak_rank, equal_to("3"))
    assert_that(varied.weeks_on_chart, equal_to("17"))
