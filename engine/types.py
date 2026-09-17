"""Type chart of the League battle engine."""

CHART = {
    ("fire", "grass"): 2.0,
    ("fire", "water"): 0.5,
    ("water", "fire"): 2.0,
    ("water", "grass"): 0.5,
    ("grass", "water"): 2.0,
    ("grass", "fire"): 0.5,
    ("ice", "grass"): 2.0,
    ("ice", "water"): 0.5,
    ("fire", "ice"): 2.0,
}


def effectiveness(attack_type, defend_type):
    """How hard a move of attack_type hits a Pokemon of defend_type."""
    return CHART.get((attack_type, defend_type), 1.0)
