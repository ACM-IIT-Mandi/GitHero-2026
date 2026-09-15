import unittest

from engine.types import multiplier


class TypeChartTest(unittest.TestCase):
    def test_fire_burns_grass(self):
        self.assertEqual(multiplier("fire", "grass"), 2.0)

    def test_water_resists_fire(self):
        self.assertEqual(multiplier("fire", "water"), 0.5)

    def test_unknown_pair_is_neutral(self):
        self.assertEqual(multiplier("fire", "fire"), 1.0)


if __name__ == "__main__":
    unittest.main()
