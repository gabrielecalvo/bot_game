import random


def strategy(bot_positions):
    return random.choices(["walk", "sabotage"], weights=[3, 7])[0]
