import streamlit as st

from bot_game import Game
import util


def app():
    st.markdown(
        """
        # Single Bot Race

        **Now it's time to race**!!!

        Click the button below to generate and show the outcome of a single Bot race.
        """
    )

    if st.button("Run Race"):
        bots = util.build_all_bots()

        game = Game(bots, use_trace=True, verbose=False)
        while game.winner is None:
            game.play_round()

        fig = util.create_animation(game.trace_df)
        st.plotly_chart(fig, use_container_width=True)
