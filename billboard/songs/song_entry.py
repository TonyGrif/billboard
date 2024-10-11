"""This module defines the information structure for each song entry."""

from dataclasses import dataclass


@dataclass(frozen=True)
class SongEntry:
    """
    Represents a chart entry for a given song.

    Attributes:
        rank (int): The rank of the song.
        title (str): The title of the song.
        artist (str): A string representing the artist(s) of the song.
        last_week_rank (str): The rank this song had last week.
        peak_rank (str): The highest rank this song has had.
        weeks_on_chart (str): The number of weeks this song has been on the chart.
    """

    rank: int
    title: str
    artist: str
    last_week_rank: str
    peak_rank: str
    weeks_on_chart: str
