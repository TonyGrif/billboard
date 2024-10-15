"""This module contains the scraper for the Aritst 100 chart."""

from datetime import datetime, timedelta
from typing import Optional

from billboard.super import Chart
from billboard.utils import Entry as ArtistEntry
from billboard.utils import make_request, parse_request


class ArtistChart(Chart):
    """
    A data structure representing a week of the artist 100 chart.

    Attributes
    ------------
    date: str
        The date for this chart in ISO 8601 format (YYYY-MM-DD).
    chart: List[ChartEntry]
        The chart for the given date containing all chart data.
    """

    def __init__(self, date: Optional[str] = None, auto_date: bool = True) -> None:
        """
        The constructor for a BillboardChart object.

        Parameters
        -----------
        date: str
            An optional date (YYYY-MM-DD) for this chart; if none is provided,
            the chart from one day ago is used.
        auto_date: bool
            Determines if the object will auto update the date to the previous
            week if the choosen one does not exist.
        """
        super().__init__(date, auto_date, "2014-07-19")

    @property
    def top_spot(self) -> ArtistEntry:
        """
        Get the top spot from this week.

        Returns
        --------
        ArtistEntry
            A data structure containing the top spot information.
        """
        return self.chart[0]

    def _generate_chart(self):
        """
        Generate the chart for the given week.
        """
        response = make_request("artist-100", self.date)
        if (data := parse_request(response)) == [] and self.auto_date is True:
            week_ago = datetime.fromisoformat(self.date) - timedelta(weeks=1)
            self.date = week_ago.strftime("%Y-%m-%d")
        else:
            self.chart = data
