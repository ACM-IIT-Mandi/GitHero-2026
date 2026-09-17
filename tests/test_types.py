import unittest

from engine.types import effectiveness


class TypeChartTest(unittest.TestCase):
    def test_fire_burns_grass(self):
        self.assertEqual(effectiveness("fire", "grass"), 2.0)

    def test_water_resists_fire(self):
        self.assertEqual(effectiveness("fire", "water"), 0.5)

    def test_unknown_pair_is_neutral(self):
        self.assertEqual(effectiveness("fire", "fire"), 1.0)

    def test_ice_freezes_grass(self):
        self.assertEqual(effectiveness("ice", "grass"), 2.0)


if __name__ == "__main__":
    unittest.main()
