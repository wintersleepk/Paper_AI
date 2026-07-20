import streamlit as st


def render_sidebar(paper):

    with st.sidebar:

        st.title("PaperMind AI")

        st.write(
            f"**Current Paper:** {paper.filename}"
        )

        st.divider()

        st.metric(
            "Pages",
            paper.pages
        )

        st.metric(
            "Reading Time",
            f"{paper.reading_time} min"
        )

        st.metric(
            "Sections",
            len(paper.sections)
        )

        st.metric(
            "Chunks",
            len(paper.chunks)
        )

        st.divider()

        st.write(
            "✅ Vector Database Ready"
            if paper.vector_ready
            else "⚠️ Vector Database Not Ready"
        )

        st.write(
            "✅ Analysis Generated"
            if paper.summary
            else "⚠️ Analysis Pending"
        )

        st.divider()

        if st.button(
            "Upload New Paper",
            use_container_width=True
        ):

            st.session_state.clear()

            st.switch_page(
                "app.py"
            )