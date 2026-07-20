import streamlit as st


def render_hero():

    st.title(
        "PaperMind AI"
    )

    st.caption(
        "AI Workspace for Research Papers"
    )

    st.write(
        """
Upload a research paper and instantly generate:

- Executive Summary
- Study Notes
- Research Insights
- Quiz Questions
- AI-powered Q&A
"""
    )

    st.divider()