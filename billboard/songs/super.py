"""This module contains the parent class for all song chart classes."""

from abc import abstractmethod
from typing import List

from billboard.super import Chart

from .song_entry import SongEntry


class SongChart(Chart):
    """
    Abstract class containing song charts interface.

    Attributes
    ----------------
    date: str
        The date for this chart in ISO 8601 format (YYYY-MM-DD).
    chart: List[ChartEntry]
        The chart for the given date containing all chart data.
    """

    @property
    def top_spot(self) -> SongEntry:
        """
        Get the top spot from this week.

        Returns
        --------
        ChartEntry
            A data structure containing the top spot information.
        """
        return self.chart[0]

    def artist_entries(self, artist: str, rank: int = 100) -> List[SongEntry]:
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
        raise NotImplementedError  # pragma: no cover
