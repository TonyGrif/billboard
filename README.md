# Billboard
Python scraper for [Billboard Hot 100](https://www.billboard.com/charts/hot-100/)

## Requirements
* [Python 3.8+](https://www.python.org/)
* [Requests](https://requests.readthedocs.io/en/latest/)
* [BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/en/latest/)

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
