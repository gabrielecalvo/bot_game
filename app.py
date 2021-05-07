"""
# Bot Race Web App
Fun little app to teach python coding to beginners.

icons: https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json

author: gabe calvo
"""
import streamlit as st

import page_home
import page_grand_prix
import page_single_race
import page_create_strategy
import page_examples
import util

st.set_page_config(page_title="Bot Race", page_icon=":rocket:", layout="wide")

PAGES = {
    "Home": page_home,
    "Create Strategy Page": page_create_strategy,
    "Examples Page": page_examples,
    "Single Race Page": page_single_race,
    "Grand Prix Page": page_grand_prix,
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

st.sidebar.markdown("#")  # separator
if st.sidebar.button("Remove All Bots"):
    util.delete_all_bots()

page = PAGES[selection]
page.app()
