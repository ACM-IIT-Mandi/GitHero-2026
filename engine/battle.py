"""Damage rules of the League battle engine."""
from engine.types import multiplier


def damage(power, attack_type, defend_type):
    """Damage of one hit."""
    return int(power * multiplier(attack_type, defend_type))


FREEZE_TURNS = 3


def can_move(status, turns_frozen):
    """A frozen Pokemon skips its turn until it thaws."""
    return not (status == "frozen" and turns_frozen < FREEZE_TURNS)
