"""
This module contains dataclasses for use by Scrapers.
"""

from .artist_entry import ArtistEntry
from .song_entry import SongEntry

__all__ = [
    "SongEntry",
    "ArtistEntry",
]
