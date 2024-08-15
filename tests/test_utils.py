from hamcrest import assert_that, contains_string

from billboard.utils import make_request


def test_make_request():
    response = make_request("2024-08-15")
    assert_that(response.text, contains_string("Shaboozey"))
