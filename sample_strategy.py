def strategy(bot_positions):
    if len(bot_positions) > 2:
        action = "sabotage"
    else:
        action = "walk"
    return action
