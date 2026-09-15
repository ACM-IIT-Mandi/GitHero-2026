"""Damage rules of the League battle engine."""
from engine.types import multiplier


def damage(power, attack_type, defend_type):
    """Damage of one hit."""
    return int(power * multiplier(attack_type, defend_type))
