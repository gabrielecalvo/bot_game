def strategy(bot_positions):
    my_position = bot_positions["BarelySmart"]
    
    n_same_position = 0
    for pos in bot_positions.values():
        if pos == my_position:
            n_same_position += 1
    
    if n_same_position > 2:
        return "sabotage"
    else:
        return "walk"