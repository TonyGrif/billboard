from datetime import datetime, timedelta

from hamcrest import any_of, assert_that, calling, equal_to, has_length, raises

from billboard import GlobalChart


class TestGlobalChart:
    def test_init(self, glob_chart):
        assert_that(glob_chart.date, equal_to("2024-08-08"))
        assert_that(glob_chart.chart, has_length(200))
        assert_that(glob_chart.oldest_date, equal_to("2020-09-12"))

        cur = GlobalChart(auto_date=False)
        yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        assert_that(cur.date, equal_to(yesterday))
        assert_that(len(cur.chart), any_of(equal_to(0), equal_to(200)))

    def test_date_exception(self):
        assert_that(calling(GlobalChart).with_args("01/01/24"), raises(ValueError))
        assert_that(calling(GlobalChart).with_args("2020-09-01"), raises(ValueError))

        not_yet = datetime.today() + timedelta(weeks=1)
        assert_that(
            calling(GlobalChart).with_args(not_yet.strftime("%Y-%m-%d")),
            raises(ValueError),
        )

    def test_top_spot(self, glob_chart):
        top = glob_chart.top_spot
        assert_that(top.rank, equal_to(1))
        assert_that(top.title, equal_to("Who"))
        assert_that(top.artist, equal_to("Jimin"))
        assert_that(top.last_week_rank, equal_to("1"))
        assert_that(top.peak_rank, equal_to("1"))
        assert_that(top.weeks_on_chart, equal_to("2"))

    def test_get_artist(self, glob_chart):
        artist = glob_chart.artist_entries("Chappell Roan", 200)
        assert_that(artist, has_length(4))

        artist = glob_chart.artist_entries("chappell roan", 200)
        assert_that(artist, has_length(4))

        artist = glob_chart.artist_entries("Chappell Roan", rank=50)
        assert_that(artist, has_length(2))
