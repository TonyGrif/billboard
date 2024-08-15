from typing import Optional
from datetime import datetime


class BillboardChart:
    """
    A data structure representing a week of Billboard Hot 100's charts.

    Attributes
    -----------
    date: str
        The date for this chart in ISO 8601 format (YYYY-MM-DD).
    chart: List[]
        The chart for the given date.
    """

    def __init__(self, date: Optional[str] = None) -> None:
        """
        The constructor for a BillboardChart object.

        Parameters
        -----------
        date: str
            An optional date (YYYY-MM-DD) for this chart; if none is provided,
            the current date is used.
        """
        if date is not None:
            self.date = date
        else:
            self.date = datetime.today().strftime("%Y-%m-%d")

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
        self._date = iso_date

    @property
    def charts(self):
        """
        Get the full chart from the given week.

        Returns
        ---------
        List
            A collection of chart data from the given week.
        """
        raise NotImplementedError

    @property
    def top_spot(self):
        """
        Get the top spot from this week.

        Returns
        --------
        TBD
            A data structure containing the top spot information.
        """
        raise NotImplementedError
