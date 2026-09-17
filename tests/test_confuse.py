import unittest

from engine.battle import after_move


class ConfuseTest(unittest.TestCase):
    def test_confused_after(self):
        self.assertEqual(after_move("outrage", 2), "confused")

    def test_fine_during(self):
        self.assertIsNone(after_move("outrage", 1))


if __name__ == "__main__":
    unittest.main()
