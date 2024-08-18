from datetime import datetime, timedelta
from typing import List, Optional

from billboard.chart_entry import ChartEntry

from .utils import make_request, parse_request


class BillboardChart:
    """
    A data structure representing a week of Billboard Hot 100's charts.

    Attributes
    -----------
    date: str
        The date for this chart in ISO 8601 format (YYYY-MM-DD).
    chart: List[ChartEntry]
        The chart for the given date containing all chart data.
    """

    def __init__(self, date: Optional[str] = None) -> None:
        """
        The constructor for a BillboardChart object.

        Parameters
        -----------
        date: str
            An optional date (YYYY-MM-DD) for this chart; if none is provided,
            the chart from one day ago is used
        """
        self.chart: List = []
        if date is not None:
            self.date = date
        else:
            self.date = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")

    @property
    def date(self) -> str:
        """
        Get the data used for the current chart.

        Returns
        --------
        str
            The ISO 8601 formatted date.
        """
        return self._date

    @date.setter
    def date(self, iso_date: str) -> None:
        """
        Set a new date for the class and update the current chart.

        Parameters
        -----------
        iso_date: str
            A ISO 8601 formatted date.

        Raises
        --------
        ValueError
            If the date is before 1958-08-04 or after the current date.
        """
        try:
            date = datetime.fromisoformat(iso_date)
        except Exception as exc:
            raise ValueError(
                "Improperly formatted ISO string, expected YYYY-MM-DD"
            ) from exc

        if date < datetime.fromisoformat("1958-08-04") or date > datetime.today():
            raise ValueError(
                "Invalid date provided, expected 1958-08-04 - Current Date"
            )

        self._date = date.strftime("%Y-%m-%d")
        self._generate_chart()

    @property
    def top_spot(self) -> ChartEntry:
        """
        Get the top spot from this week.

        Returns
        --------
        ChartEntry
            A data structure containing the top spot information.
        """
        return self.chart[0]

    def _generate_chart(self):
        """
        Generate the chart for the given week.
        """
        response = make_request(self.date)
        self.chart = parse_request(response)
