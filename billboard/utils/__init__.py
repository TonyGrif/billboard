"""
This module contains the functions and dataclasses for scrapers.

Classes
--------
    AlbumEntry
    ArtistEntry
    SongEntry

Functions
---------
    make_request
    parse_song_request
    parse_artist_request
    parse_album_request
"""

from .dataclasses import AlbumEntry, ArtistEntry, SongEntry
from .funcs import (
    make_request,
    parse_album_request,
    parse_artist_request,
    parse_song_request,
)

__all__ = [
    "AlbumEntry",
    "ArtistEntry",
    "SongEntry",
    "make_request",
    "parse_album_request",
    "parse_artist_request",
    "parse_song_request",
]
