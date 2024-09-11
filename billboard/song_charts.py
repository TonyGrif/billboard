from typing import List, Optional

from billboard.songs import BillboardChart, GlobalChart
from billboard.songs.chart_entry import ChartEntry


class SongCharts:
    """
    Class to manage all song charts available.

    Attributes:
        date (str): The date for the charts in ISO 8601 format (YYYY-MM-DD)
        hot100 (BillboardChart): The Hot 100 chart.
        global200 (GlobalChart): The Global 200 chart.
    """

    def __init__(self, date: Optional[str] = None) -> None:
        """
        The constructor for the SongCharts.

        Parameters:
            date (str): An optional date (YYYY-MM-DD) for this chart; if none is 
                provided, the chart from one day ago is used.
        """
        self.hot100 = BillboardChart(date)
        self.global200 = GlobalChart(date)

    @property
    def hot_chart(self) -> List[ChartEntry]:
        """
        Return the Hot 100 chart.

        Returns:
            A list containing ChartEntry elements.
        """
        return self.hot100.chart

    @property
    def global_chart(self) -> List[ChartEntry]:
        """
        Return the Global 200 chart.

        Returns:
            A list containing ChartEntry elements.
        """
        return self.global200.chart
