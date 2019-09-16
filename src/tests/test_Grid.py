import unittest
from Grid import Grid
from Site import Site

class GridTestCase(unittest.TestCase):

    def test_containes_GivenSiteThatBelongsToGrid_ThenReturnTrue(self):
        grid = Grid(3)
        self.assertTrue(grid.contains(Site(2,2)))

    def test_containes_GivenSiteThatDoesNotBelongToGrid_ThenReturnFalse(self):
        grid = Grid(3)
        self.assertFalse(grid.contains(Site(4,4)))