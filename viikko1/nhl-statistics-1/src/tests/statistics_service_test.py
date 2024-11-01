import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class testStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())
        
    def test_search_tuntematon(self):
        self.assertEqual(None, self.stats.search("tuntematon"))

    def test_search_tunnettu(self):
        self.assertEqual("Semenko", self.stats.search("Semenko").name)

    def test_search_tiimi(self):
        self.assertEqual(3, len(self.stats.team("EDM")))

    def test_top(self):
        self.assertEqual(35, self.stats.top(1)[0].goals)

    def test_top_sorttaaPOINTS(self):
        self.assertEqual(35, self.stats.top(1, SortBy.POINTS)[0].goals)

    def test_top_sorttaaGOALS(self):
        self.assertEqual(45, self.stats.top(1, SortBy.GOALS)[0].goals)

    def test_top_sorttaaASSISTS(self):
        self.assertEqual(89, self.stats.top(1, SortBy.ASSISTS)[0].assists)
