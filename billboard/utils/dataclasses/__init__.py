"""
This module contains dataclasses for use by Scrapers.
"""

from .album_entry import AlbumEntry
from .artist_entry import ArtistEntry
from .song_entry import SongEntry

__all__ = [
    "AlbumEntry",
    "SongEntry",
    "ArtistEntry",
]
