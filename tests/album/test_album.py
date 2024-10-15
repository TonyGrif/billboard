from datetime import datetime, timedelta

from hamcrest import any_of, assert_that, calling, equal_to, has_length, raises

from billboard import AlbumChart


class TestAlbumChart:
    def test_init(self, album_chart):
        assert_that(album_chart.date, equal_to("2024-08-08"))
        assert_that(album_chart.chart, has_length(200))
        assert_that(album_chart.oldest_date, equal_to("1963-08-17"))

        cur = AlbumChart(auto_date=False)
        yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        assert_that(cur.date, equal_to(yesterday))
        assert_that(len(cur.chart), any_of(equal_to(0), equal_to(100)))

    def test_date_exception(self):
        assert_that(calling(AlbumChart).with_args("01/01/24"), raises(ValueError))

        assert_that(calling(AlbumChart).with_args("1958-07-04"), raises(ValueError))

        not_yet = datetime.today() + timedelta(weeks=1)
        assert_that(
            calling(AlbumChart).with_args(not_yet.strftime("%Y-%m-%d")),
            raises(ValueError),
        )

    def test_top_spot(self, album_chart):
        top = album_chart.top_spot
        assert_that(top.rank, equal_to(1))
        assert_that(top.title, equal_to("The Tortured Poets Department"))
        assert_that(top.artist, equal_to("Taylor Swift"))
        assert_that(top.last_week_rank, equal_to("4"))
        assert_that(top.peak_rank, equal_to("1"))
        assert_that(top.weeks_on_chart, equal_to("15"))
