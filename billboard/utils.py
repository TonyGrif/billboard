from typing import Optional

import requests

URL: str = "https://www.billboard.com/charts/hot-100/"


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
