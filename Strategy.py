from random import randint

def unbeatable_strategy(remaining, max_turn):
    if remaining <= 3:
        return remaining
    mod = remaining % (max_turn + 1)
    return max(mod, 1)

def random_strategy(remaining, max_turn):
    return randint(1, min(max_turn,remaining))
