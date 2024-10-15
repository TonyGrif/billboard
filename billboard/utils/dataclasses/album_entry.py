"""This module defines the information structure for each album entry."""

from dataclasses import dataclass


@dataclass(frozen=True)
class AlbumEntry:
    """
    Represents a chart entry for a given album.

    Attributes:
        rank (int): The rank of the album.
        title (str): The title of the album.
        artist (str): A string representing the artist(s) of the album.
        last_week_rank (str): The rank this album had last week.
        peak_rank (str): The highest rank this album has had.
        weeks_on_chart (str): The number of weeks this album has been on the chart.
    """

    rank: int
    title: str
    artist: str
    last_week_rank: str
    peak_rank: str
    weeks_on_chart: str
