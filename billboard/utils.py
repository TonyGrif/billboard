from typing import List, Optional

import requests
from bs4 import BeautifulSoup

URL: str = "https://www.billboard.com/charts/hot-100/"
CHART_RESULT_SELECTOR = (
    "chart-results-list // lrv-u-padding-t-150 lrv-u-padding-t-050@mobile-max"
)
RESULT_CONTAINER = "o-chart-results-list-row-container"


def make_request(date: str, timeout: Optional[int] = 5) -> requests.Response:
    """
    Make the HTTP request of the Billboard Hot 100 site.

    Parameters
    -----------
    date: str
        The date of the chart to gather.
    timeout: int
        An optional integer to specify the timeout for making the request; the
        default value if 5 seconds.

    Returns
    ---------
    requests.Response
        The response object from the HTTP GET request.

    Raises
    ----------
    HTTPError
        On a non-successful status code being returned.
    """
    response = requests.get(f"{URL}/{date}", timeout=timeout)
    response.raise_for_status()
    return response


def parse_request(response: requests.Response) -> List:
    """
    Parse the HTTP response for chart data.

    Parameters
    ----------
    response: requests.Response
        The HTTP response generated from the Billboard Hot 100 site.

    Returns
    ---------
    List
        Collection containing each chart entry.
    """
    container = _get_container(response.text)
    return _get_results(str(container))


def _get_container(text: str):
    soup = BeautifulSoup(text, "html.parser")
    return soup.find("div", {"class": CHART_RESULT_SELECTOR})


def _get_results(text: str) -> List:
    soup = BeautifulSoup(text, "html.parser")
    return soup.find_all("div", {"class": RESULT_CONTAINER})
