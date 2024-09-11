from typing import List, Optional

import requests
from bs4 import BeautifulSoup

from .songs.chart_entry import ChartEntry

URL: str = "https://www.billboard.com/charts/hot-100/"
CHART_RESULT_SELECTOR = (
    "chart-results-list // lrv-u-padding-t-150 lrv-u-padding-t-050@mobile-max"
)
RESULT_CONTAINER = "o-chart-results-list-row-container"
RANKING = (
    "c-label a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet"
)
DETAILS_CLASS = "lrv-u-width-100p"


def make_request(date: str, timeout: Optional[int] = 5) -> requests.Response:
    """
    Make the HTTP request of the Billboard Hot 100 site.

    Parameters
    -----------
    date: str
        The date of the chart to gather.
    timeout: int
        An optional integer to specify the timeout for making the request; the
        default value is 5 seconds.

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


def parse_request(response: requests.Response) -> List[ChartEntry]:
    """
    Parse the HTTP response for chart data.

    Parameters
    ----------
    response: requests.Response
        The HTTP response generated from the Billboard Hot 100 site.

    Returns
    ---------
    List[ChartEntry]
        Collection containing each chart entry.
    """
    if (container := _get_container(response.text)) != []:
        return _get_data(str(container))
    return []


def _get_container(text: str):
    soup = BeautifulSoup(text, "html.parser")
    return soup.find("div", {"class": CHART_RESULT_SELECTOR})


def _get_data(text: str) -> List[ChartEntry]:
    data: List = []

    soup = BeautifulSoup(text, "html.parser")
    for block in soup.find_all("div", {"class": RESULT_CONTAINER}):
        data.append(_parse_block(str(block)))
    return data


def _parse_block(text: str) -> ChartEntry:
    soup = BeautifulSoup(text, "html.parser")

    if (rank_html := soup.find("span", {"class": RANKING})) is not None:
        rank = int(rank_html.get_text(strip=True))
    else:
        raise ValueError("Unable to find rank")

    if (details_str := soup.find("li", {"class": DETAILS_CLASS})) is not None:
        details = details_str.get_text(separator="\\", strip=True).split("\\")
    else:
        raise ValueError("Unable to find title and artist(s) details")

    return ChartEntry(
        rank, details[0], details[1], details[-3], details[-2], details[-1]
    )
