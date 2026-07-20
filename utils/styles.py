import streamlit as st


def load_css():

    try:

        with open(
            "assets/styles.css",
            encoding="utf-8"
        ) as file:

            st.markdown(

                f"<style>{file.read()}</style>",

                unsafe_allow_html=True

            )

    except FileNotFoundError:

        st.warning(
            "styles.css not found."
        )