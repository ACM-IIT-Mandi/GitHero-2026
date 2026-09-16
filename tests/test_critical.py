import unittest

from engine.battle import critical


class CriticalTest(unittest.TestCase):
    def test_neutral(self):
        self.assertEqual(critical(40, "fire", "fire"), 60)

    def test_ignores_resistance(self):
        self.assertEqual(critical(40, "fire", "water"), 60)

    def test_keeps_weakness(self):
        self.assertEqual(critical(40, "fire", "grass"), 120)


if __name__ == "__main__":
    unittest.main()
