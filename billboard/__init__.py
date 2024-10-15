"""This module contains scrapers for the Billboard music charts site.

Classes
--------
    SongCharts
    BillboardChart
    GlobalChart
    ArtistChart
    AlbumChart
"""

from .album import AlbumChart
from .artists import ArtistChart
from .songs import BillboardChart, GlobalChart, SongCharts

__all__ = [
    "SongCharts",
    "BillboardChart",
    "GlobalChart",
    "ArtistChart",
    "AlbumChart",
]
