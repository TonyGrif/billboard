from dataclasses import dataclass


@dataclass(frozen=True)
class ArtistEntry:
    """
    Represents a chart entry for a given artist.

    Attributes:
        rank (int): The rank of the artist.
        artist (str): A string representing the artist.
        last_week_rank (str): The rank had last week.
        peak_rank (str): The highest rank this artist has had.
        weeks_on_chart (str): The number of weeks this artist has been on the chart.
    """

    rank: int
    artist: str
    last_week_rank: str
    peak_rank: str
    weeks_on_chart: str
