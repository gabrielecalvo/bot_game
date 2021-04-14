import streamlit as st

import util


def app():
    st.markdown(
        """
        # Bot Game - Upload

        **Upload your strategy**!!!

        All you need to do is **upload a python file** with your name (e.g. `Gabe.py`).
        The file should contain a function called `strategy` that takes in a
        dictionary named `bot_positions` as argument and returns either
        "walk" or "sabotage".

        For example:
        ```python
        def strategy(bot_positions):
            if len(bot_positions) > 2:
                action = "sabotage"
            else:
                action = "walk"
            return action
        ```
        """
    )

    file_buffer = st.file_uploader("Upload a strategy file (.py)")
    if file_buffer:
        fp = util.save_file(filename=file_buffer.name, filebytes=file_buffer.getvalue())
        util.validate_file(fp)
        st.success(
            "File uploaded and validated successfully, "
            "go to `Race Page` to run the Game"
        )

    competitors = util.build_all_bots()
    formatted_competitors = "\n".join([f"\t- {c}" for c in competitors])
    st.markdown(f"### Current Competitors:\n{formatted_competitors}")
