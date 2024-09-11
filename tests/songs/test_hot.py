from datetime import datetime, timedelta

from hamcrest import any_of, assert_that, calling, equal_to, has_length, raises

from billboard import BillboardChart


class TestBillboardChart:
    def test_init(self, hot_chart):
        assert_that(hot_chart.date, equal_to("2024-08-08"))
        assert_that(hot_chart.chart, has_length(100))

        cur = BillboardChart(auto_date=False)
        yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        assert_that(cur.date, equal_to(yesterday))
        assert_that(len(cur.chart), any_of(equal_to(0), equal_to(100)))

    def test_date_exception(self):
        assert_that(calling(BillboardChart).with_args("01/01/24"), raises(ValueError))

        assert_that(calling(BillboardChart).with_args("1958-07-04"), raises(ValueError))

        not_yet = datetime.today() + timedelta(weeks=1)
        assert_that(
            calling(BillboardChart).with_args(not_yet.strftime("%Y-%m-%d")),
            raises(ValueError),
        )

    def test_top_spot(self, hot_chart):
        top = hot_chart.top_spot
        assert_that(top.rank, equal_to(1))
        assert_that(top.title, equal_to("A Bar Song (Tipsy)"))
        assert_that(top.artist, equal_to("Shaboozey"))
        assert_that(top.last_week_rank, equal_to("1"))
        assert_that(top.peak_rank, equal_to("1"))
        assert_that(top.weeks_on_chart, equal_to("16"))

    def test_get_artist(self, hot_chart):
        artist = hot_chart.artist_entries("Chappell Roan")
        assert_that(artist, has_length(6))

        artist = hot_chart.artist_entries("chappell roan")
        assert_that(artist, has_length(6))

        artist = hot_chart.artist_entries("Chappell Roan", rank=50)
        assert_that(artist, has_length(3))
