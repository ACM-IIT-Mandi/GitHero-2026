"""Damage rules of the League battle engine."""
from engine.types import multiplier


def damage(power, attack_type, defend_type):
    """Damage of one hit."""
    return int(power * multiplier(attack_type, defend_type))


FREEZE_TURNS = 2


def can_move(status, turns_frozen):
    """A frozen Pokemon skips its turn until it thaws."""
    return not (status == "frozen" and turns_frozen < FREEZE_TURNS)


def critical(power, attack_type, defend_type):
    """A critical hit ignores a resisted match-up."""
    return int(power * 1.5 * max(1.0, multiplier(attack_type, defend_type)))


def counter(damage_taken):
    """Counter returns double the last hit taken."""
    return damage_taken * 2


STAGE_BONUS = 0.5


def boosted(power, stages):
    """Dragon Dance raises attack by one stage per use."""
    return int(power * (1 + STAGE_BONUS * stages))


OUTRAGE_TURNS = 2


def locked_in(move, turns_used):
    """Outrage locks the user in for two turns."""
    return move == "outrage" and turns_used < OUTRAGE_TURNS


def after_move(move, turns_used):
    """Outrage confuses the user when it ends."""
    return "confused" if move == "outrage" and turns_used >= OUTRAGE_TURNS else None
