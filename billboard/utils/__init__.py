"""
This module contains the functions and dataclasses for scrapers.

Classes
--------
    ArtistEntry
    SongEntry

Functions
---------
    make_request
    parse_request
    parse_artist_request
"""

from .dataclasses import ArtistEntry, SongEntry
from .funcs import make_request, parse_artist_request, parse_request

__all__ = [
    "ArtistEntry",
    "SongEntry",
    "make_request",
    "parse_request",
    "parse_artist_request",
]
