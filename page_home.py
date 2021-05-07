import streamlit as st


def app():
    st.markdown(
        """
    # Welcome to the Bot Race
    *The excitement is high and the tension is palpable! Many aspire to win 
    the Bot Grand Prix, but who will beat all competition?*

    :rocket::rocket::rocket:

    In this game you will **code up a strategy** that your Bot will follow to
    try to get to the *end of the race first* (reach **position 10**).

    Each turn a Bot can either of the following *actions**:
    - **walk** :runner:: move forward one position
    - **sabotage** :hammer:: turn other bots currently at the same position 
        as its own so they are facing backwards

    Each round, the order in which the competing Bots take turns to perform their
    action is *randomised* and at the beginning of the round all bots are *reset
    to face forwards*.

    Go on to the **Create Strategy Page** to define your strategy.
    """
    )
