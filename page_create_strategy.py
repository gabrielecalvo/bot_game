import streamlit as st
import inspect
import util


def app():
    st.markdown(
        """
        # Create Strategy

        Here you can create your strategy!

        You will need to create a function called `strategy` that takes in a
        dictionary named `bot_positions` (e.g. `{"Bot1": 1, "Bot2": 3}`) as argument
        and should return either *"walk"* or *"sabotage"*.

        See the ***Example page*** for examples.

        You can either:
        """
    )

    with st.beta_expander("Write Code Directly"):
        bot_name = st.text_input(label="Bot Name")
        strategy_code = st.text_area(
            label="Strategy Code: ",
            value=inspect.cleandoc(
                """
        import random
            
        def strategy(bot_positions):
            return random.choice(["walk", "sabotage"])
        """
            ),
            height=320,
        )
        if st.button("Submit"):
            if bot_name:
                fp = util.save_code_to_file(code=strategy_code, filename=bot_name)
                util.validate_file(fp)
                st.success(
                    "File uploaded and validated successfully, "
                    "go to `Race Page` to run the Game"
                )
            else:
                st.error("Please provide a name for the Bot")

    with st.beta_expander("Upload a file"):
        file_buffer = st.file_uploader(
            "Upload a strategy file (.py)",
            help="The filename will be used to name the Bot",
        )
        if file_buffer:
            fp = util.save_file(
                filename=file_buffer.name, filebytes=file_buffer.getvalue()
            )
            util.validate_file(fp)
            st.success(
                "File uploaded and validated successfully, "
                "go to `Race Page` to run the Game"
            )

    st.markdown(f"## Current Competitors:")
    competitors = util.build_all_bots()
    if competitors:
        st.markdown("\n".join([f"\t- {c}" for c in competitors]))
    else:
        st.markdown("no competitors saved yet")

    if st.button("Add example bots"):
        util.add_example_bots()
        st.experimental_rerun()
