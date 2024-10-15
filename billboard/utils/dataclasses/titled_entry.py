"""This module defines the information structure for each entry containing a title."""

from dataclasses import dataclass

from .entry import Entry


@dataclass(frozen=True)
class TitledEntry(Entry):
    """
    Represents a chart entry for a given song.

    Attributes:
        rank (int): The rank of the entry.
        title (str): The title of the entry.
        artist (str): A string representing the artist(s) of the entry.
        last_week_rank (str): The rank this entry had last week.
        peak_rank (str): The highest rank this entry has had.
        weeks_on_chart (str): The number of weeks this entry has been on the chart.
    """

    title: str
