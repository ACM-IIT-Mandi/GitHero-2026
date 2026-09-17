import unittest

from engine.battle import FREEZE_TURNS, can_move


class FreezeTest(unittest.TestCase):
    def test_frozen_skips(self):
        self.assertFalse(can_move("frozen", 0))

    def test_thaws(self):
        self.assertTrue(can_move("frozen", FREEZE_TURNS))

    def test_healthy_moves(self):
        self.assertTrue(can_move(None, 0))


if __name__ == "__main__":
    unittest.main()
