import streamlit as st

import util
from bot_game import grand_prix


def app():
    st.markdown(
        """
        # Bot Game - Grand Prix

        **Now it's time to race**!!!

        Select how many races you want to perform and let the grand-prix begin!
        """
    )

    lcol, rcol = st.beta_columns([2, 1])
    n_races = lcol.number_input(
        "Number of races: ", min_value=1, max_value=100_000, value=1000
    )
    rcol.title("")  # just for spacing

    if rcol.button("Start Grand Prix"):
        bots = util.build_all_bots()
        prog_bar = st.progress(0)
        winnings = grand_prix(bots, n=n_races, prog_bar=prog_bar)
        winning_dict = {str(k): v for k, v in winnings.items()}

        fig = util.plot_grand_prix_results(winning_dict)
        st.plotly_chart(fig)
