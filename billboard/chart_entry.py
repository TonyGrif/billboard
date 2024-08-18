from dataclasses import dataclass


@dataclass(frozen=True)
class ChartEntry:
    rank: str
    title: str
    artist: str
    last_week_rank: str
    peak_rank: str
    weeks_on_chart: str
