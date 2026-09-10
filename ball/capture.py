def catch_chance(rate, hp_left):
    return min(1.0, rate * (1.5 - hp_left))
