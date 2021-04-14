original_list = ['walk', 'walk', 'sabotage']
current_list = []

def strategy(bot_positions):
    global current_list  # to allow "write-access" to out-of-function variables
    
    if current_list == []:
        current_list = original_list.copy()
    return current_list.pop(0)
