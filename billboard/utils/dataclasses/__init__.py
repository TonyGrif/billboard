"""
This module contains dataclasses for use by Scrapers.
"""

from .entry import Entry as ArtistEntry
from .titled_entry import TitledEntry as AlbumEntry  # pylint: disable=W0404
from .titled_entry import TitledEntry as SongEntry  # pylint: disable=W0404

__all__ = [
    "ArtistEntry",
    "SongEntry",
    "AlbumEntry",
]
