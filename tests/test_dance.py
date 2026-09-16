import unittest

from engine.battle import boosted


class DanceTest(unittest.TestCase):
    def test_one_stage(self):
        self.assertEqual(boosted(40, 1), 60)

    def test_no_stage(self):
        self.assertEqual(boosted(40, 0), 40)


if __name__ == "__main__":
    unittest.main()
