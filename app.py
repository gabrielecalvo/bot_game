import streamlit as st

import race_page
import upload_page

st.set_page_config(page_title="Bot Race", page_icon=":rocket:", layout="wide")

PAGES = {
    "Upload Page": upload_page,
    "Race Page": race_page,
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
