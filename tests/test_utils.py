import pytest
from hamcrest import assert_that, contains_string, has_length

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
