"""This module contains a bundled class containing both the Hot 100
and Global 200 scrapers.
"""

from typing import List, Optional

from billboard.utils import TitledEntry as SongEntry

from ..songs import BillboardChart, GlobalChart


class SongCharts:
    """Class to manage all song charts available.

    Attributes:
        date: The date for the charts in ISO 8601 format (YYYY-MM-DD)
        auto_gen: Determines if the charts should auto generate.
        hot100 (BillboardChart): The Hot 100 chart.
        global200 (GlobalChart): The Global 200 chart.
    """

    def __init__(self, date: Optional[str] = None, auto_gen: bool = True) -> None:
        """The constructor for the SongCharts.

        Args:
            date: An optional date (YYYY-MM-DD); if none is provided, yesterday is used.
        """
        self.auto_gen = auto_gen

        if self.auto_gen:
            self.hot100 = BillboardChart(date)
            self.global200 = GlobalChart(date)
        else:
            self.hot100 = BillboardChart(date, auto_gen=False)
            self.global200 = GlobalChart(date, auto_gen=False)

    @property
    def hot_chart(self) -> List[SongEntry]:
        """Return the Hot 100 chart.

        Returns:
            A list containing SongEntry elements.
        """
        return self.hot100.chart

    @property
    def global_chart(self) -> List[SongEntry]:
        """Return the Global 200 chart.

        Returns:
            A list containing SongEntry elements.
        """
        return self.global200.chart

    def generate_charts(self):
        self.hot100.generate_chart()
        self.global200.generate_chart()
