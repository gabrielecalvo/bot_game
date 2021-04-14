import random


def strategy(bot_positions):
    return random.choices(["walk", "sabotage"], weights=[7, 3])[0]
