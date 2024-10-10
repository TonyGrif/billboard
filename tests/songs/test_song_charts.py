from hamcrest import assert_that, has_length, instance_of

from billboard.songs import BillboardChart, GlobalChart


class TestSongCharts:
    def test_hot(self, songs):
        assert_that(songs.hot100, instance_of(BillboardChart))
        assert_that(songs.hot_chart, has_length(100))

    def test_global(self, songs):
        assert_that(songs.global200, instance_of(GlobalChart))
        assert_that(songs.global_chart, has_length(200))
