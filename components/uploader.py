import streamlit as st


def render_uploader():

    return st.file_uploader(
        "Upload a PDF",
        type=["pdf"]
    )