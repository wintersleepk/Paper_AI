import streamlit as st

from services.rag_service import RAGService


rag = RAGService()


def render_chat(paper):

    for item in paper.chat_history:

        with st.chat_message("user"):

            st.markdown(
                item["question"]
            )

        with st.chat_message("assistant"):

            st.markdown(
                item["answer"]
            )

    question = st.chat_input(
        "Ask anything about this paper..."
    )

    if not question:

        return

    with st.chat_message("user"):

        st.markdown(
            question
        )

    with st.spinner(
        "Thinking..."
    ):

        answer = rag.ask(
            paper,
            question
        )

    with st.chat_message("assistant"):

        st.markdown(
            answer
        )

    st.session_state.paper = paper

    st.rerun()