import streamlit as st

import util
from bot_game import grand_prix


def app():
    st.markdown(
        """
        # Grand Prix

        **Let the big competition begin**!!!

        Select how many races you want to perform and let the grand-prix begin!
        """
    )

    lcol, rcol = st.beta_columns([2, 1])
    n_races = lcol.number_input(
        "Number of races: ", min_value=1, max_value=10_000, value=100
    )
    rcol.title("")  # just for spacing

    if rcol.button("Start Grand Prix"):
        bots = util.build_all_bots()
        prog_bar = st.progress(0)
        winnings = grand_prix(bots, n=n_races, prog_bar=prog_bar)
        winning_dict = {str(k): v for k, v in winnings.items()}

        fig = util.plot_grand_prix_results(winning_dict)
        st.plotly_chart(fig)
