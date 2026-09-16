import unittest

from engine.battle import locked_in


class OutrageTest(unittest.TestCase):
    def test_locked(self):
        self.assertTrue(locked_in("outrage", 1))

    def test_released(self):
        self.assertFalse(locked_in("outrage", 2))


if __name__ == "__main__":
    unittest.main()
