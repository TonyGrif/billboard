# Billboard
Python scraper for [Billboard Charts](https://www.billboard.com/)

## Requirements
* [Python 3.9+](https://www.python.org/)

All dependencies can be resolved through [poetry](https://python-poetry.org/)
(`poetry install`)

## Quickstart
```python
from billboard import SongCharts

chart = SongCharts("YYYY-MM-DD")

hot100 = chart.hot_chart
global200 = chart.global_chart
```

Individual charts can also be imported separately to scrape just the specific chart.
```python
from billboard import BillboardChart, GlobalChart

hot = BillboardChart("YYYY-MM-DD")
glob = GlobalChart("YYYY-MM-DD")
```

## Docs
Coming soon!
