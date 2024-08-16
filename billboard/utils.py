from typing import List, Optional

import requests
from bs4 import BeautifulSoup

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
    return _get_blocks(str(container))


def _get_container(text: str):
    soup = BeautifulSoup(text, "html.parser")
    return soup.find("div", {"class": CHART_RESULT_SELECTOR})


def _get_blocks(text: str) -> List:
    data: List = []

    soup = BeautifulSoup(text, "html.parser")
    for block in soup.find_all("div", {"class": RESULT_CONTAINER}):
        data.append(_parse_block(str(block)))
    return data


def _parse_block(text: str) -> str:
    soup = BeautifulSoup(text, "html.parser")

    rank_html = soup.find("span", {"class": RANKING})
    if rank_html is not None:
        rank = rank_html.get_text(strip=True)
    else:
        raise ValueError("Unable to find rank")

    details = soup.find("li", {"class": DETAILS_CLASS})
    if details is not None:
        det_list = details.get_text(separator="\\", strip=True).split("\\")
    else:
        raise ValueError("Unable to find title and artist(s) details")

    return f"{rank}\\{det_list[0]}\\{det_list[1]}"
