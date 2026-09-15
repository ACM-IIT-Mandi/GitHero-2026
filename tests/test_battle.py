import unittest

from engine.battle import damage


class DamageTest(unittest.TestCase):
    def test_neutral(self):
        self.assertEqual(damage(40, "fire", "fire"), 40)

    def test_super_effective(self):
        self.assertEqual(damage(40, "fire", "grass"), 80)


if __name__ == "__main__":
    unittest.main()
