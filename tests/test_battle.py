import unittest

from engine.battle import damage


class DamageTest(unittest.TestCase):
    def test_neutral(self):
        self.assertEqual(damage(40, "fire", "fire"), 40)

    def test_super_effective(self):
        self.assertEqual(damage(40, "fire", "grass"), 80)

    def test_never_below_one(self):
        self.assertEqual(damage(1, "fire", "water"), 1)


if __name__ == "__main__":
    unittest.main()
