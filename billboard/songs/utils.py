from typing import List, Optional

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent  # type: ignore

from .song_entry import SongEntry

URL: str = "https://www.billboard.com/charts"
RESULT_CONTAINER = "o-chart-results-list-row-container"
RANKING = (
    "c-label a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet"
)
DETAILS_CLASS = "lrv-u-width-100p"


def make_request(
    chart: str, date: str, timeout: Optional[int] = 5
) -> requests.Response:
    """
    Make the HTTP request of the Billboard Hot 100 site.

    Parameters
    -----------
    chart: str
        The chart to request (hot-100 or billboard-global-200).
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
    print(f"{URL}/{chart}")
    ua = UserAgent()
    header = {"User-Agent": str(ua.random)}
    response = requests.get(f"{URL}/{chart}/{date}", headers=header, timeout=timeout)
    response.raise_for_status()
    return response


def parse_request(response: requests.Response) -> List[SongEntry]:
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
    data: List = []

    soup = BeautifulSoup(response.text, "html.parser")
    for block in soup.find_all("div", {"class": RESULT_CONTAINER}):
        data.append(_parse_song_block(str(block)))
    return data


def _parse_song_block(text: str) -> SongEntry:
    soup = BeautifulSoup(text, "html.parser")
    data: List = []

    if (rank_html := soup.find("span", {"class": RANKING})) is not None:
        data.append(int(rank_html.get_text(strip=True)))
    else:
        data.append(None)

    if (details_str := soup.find("li", {"class": DETAILS_CLASS})) is not None:
        details = details_str.get_text(separator="\\", strip=True).split("\\")
        data.extend(details[0:2])
        data.extend(details[-3:])
    else:
        data.extend([None for _ in range(5)])

    return SongEntry(*data)
