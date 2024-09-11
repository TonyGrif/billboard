from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import List, Optional

from .chart_entry import ChartEntry


class SongChart(ABC):
    """
    Abstract class containing song charts interface.

    Attributes
    ----------------
    date: str
        The date for this chart in ISO 8601 format (YYYY-MM-DD).
    chart: List[ChartEntry]
        The chart for the given date containing all chart data.
    """

    def __init__(
        self,
        date: Optional[str] = None,
        auto_date: bool = True,
        oldest_date: str = "1958-08-04",
    ) -> None:
        """
        The constructor for a Chart object.

        Parameters
        -----------
        date: str
            An optional date (YYYY-MM-DD) for this chart; if none is provided,
            the chart from one day ago is used.
        auto_date: bool
            Determines if the object will auto update the date to the previous
            week if the choosen one does not exist.
        oldest_date: str
            Set the oldest date allowed for a given chart, defaults to the oldest
            available for the Hot 100 chart.
        """
        self.chart: List[ChartEntry] = []
        self.auto_date = auto_date
        self.oldest_date = oldest_date
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
            The ISO 8601 string.
        """
        try:
            date = datetime.fromisoformat(iso_date)
        except Exception as exc:
            raise ValueError(
                "Improperly formatted ISO string, expected YYYY-MM-DD"
            ) from exc

        if date < datetime.fromisoformat(self.oldest_date) or date > datetime.today():
            raise ValueError("Invalid date provided")

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

    def artist_entries(self, artist: str, rank: int = 100) -> List[ChartEntry]:
        """
        Get the entries an artist has on this chart.

        Parameters
        -----------
        artist: str
            The artists name.
        rank: int
            An optional variable for specifying an end value on ranking.

        Returns
        -------
        List[ChartEntry]
            A List containing all entries this artist has.
        """
        return [
            entry
            for entry in self.chart
            if entry.artist.lower() == artist.lower() and entry.rank <= rank
        ]

    @abstractmethod
    def _generate_chart(self):
        """
        Generate the chart for the given week.
        """
        pass
