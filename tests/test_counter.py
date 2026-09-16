import unittest

from engine.battle import counter


class CounterTest(unittest.TestCase):
    def test_doubles(self):
        self.assertEqual(counter(35), 70)


if __name__ == "__main__":
    unittest.main()
