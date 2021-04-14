import streamlit as st

def app():
    st.markdown(
        """
        # Example bots

        ## Random bot
        ```python
        def strategy(bot_positions):
            return random.choice(["walk", "sabotage"])
        ```
        
        ## List Bot
        This bot is based on a list of action that gets 
        repeated indefinitely.
        ```python
        original_list = ['walk', 'walk', 'sabotage']
        current_list = []
        def strategy(bot_positions):
            if current_list == []:
                current_list = original_list.copy()
            return random.choice(current_list.pop(0))
        ```
        
        ## Barely Smart bot
        A bot that counts how many other bots are at the same position and 
        if there are more than 2 (including itself) it uses sabotage.
        ```python
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
        ```
        ***Note**: Assuming the file is called `BarelySmart.py`, then the position of 
        the bot can be retrieved using `bot_positions["BarelySmart"]`
        """
    )