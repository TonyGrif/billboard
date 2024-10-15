"""This module defines the information structure for each entry."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Entry:
    """
    Represents a chart entry.

    Attributes:
        rank (int): The rank of the entry.
        artist (str): A string representing the artist(s) of the entry.
        last_week_rank (str): The rank this entry had last week.
        peak_rank (str): The highest rank this entry has had.
        weeks_on_chart (str): The number of weeks this entry has been on the chart.
    """

    rank: int
    artist: str
    last_week_rank: str
    peak_rank: str
    weeks_on_chart: str
