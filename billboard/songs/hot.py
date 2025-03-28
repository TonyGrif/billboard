"""This module contains the scraper for the Hot 100."""

from datetime import datetime, timedelta
from typing import Optional

from billboard.utils import make_request, parse_titled_request

from .super import SongChart


class BillboardChart(SongChart):
    """A data structure representing a week of Billboard Hot 100's charts.

    Attributes:
        date: The date for this chart in ISO 8601 format (YYYY-MM-DD).
        chart: The chart for the given date containing all chart data.
        auto_gen: Determines if the charts should be auto generated.
        auto_date: Determines if the object will auto update the date to the
            previous week if the chosen one does not exist.
        oldest_date: The oldest date allowed for a given chart.
    """

    def __init__(
        self, date: Optional[str] = None, auto_gen: bool = True, auto_date: bool = True
    ) -> None:
        """The constructor for a BillboardChart object.

        Args:
            date: An optional date (YYYY-MM-DD); if none is provided, yesterday is used.
            auto_date: Determines if the object will auto update the date to the
                previous week if the choosen one does not exist.
        """
        super().__init__(date, auto_gen, auto_date, "1958-08-04")

    def generate_chart(self):
        """Generate the chart for the given week."""
        response = make_request("hot-100", self.date)
        if (data := parse_titled_request(response)) == [] and self.auto_date is True:
            week_ago = datetime.fromisoformat(self.date) - timedelta(weeks=1)
            self.date = week_ago.strftime("%Y-%m-%d")
            self.generate_chart()
        else:
            self.chart = data
