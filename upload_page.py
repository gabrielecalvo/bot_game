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
        # assuming the file is called `BarelySmart.py`
        
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
