import streamlit as st

from components.sidebar import render_sidebar
from components.chat import render_chat
from components.export import render_export

from utils.styles import load_css

from services.analysis_service import AnalysisService
from services.vector_service import VectorService


analysis = AnalysisService()
vector = VectorService()

st.set_page_config(
    page_title="PaperMind AI",
    layout="wide"
)

load_css()

# ----------------------------
# Validate session
# ----------------------------

if (
    "paper" not in st.session_state
    or st.session_state.paper is None
):
    st.switch_page("app.py")

paper = st.session_state.paper

render_sidebar(paper)

# ----------------------------
# Header
# ----------------------------

st.title(
    paper.title if paper.title else paper.filename
)

if paper.authors:
    st.caption(", ".join(paper.authors))

# ----------------------------
# Metrics
# ----------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Pages", paper.pages)

with c2:
    st.metric("Reading Time", f"{paper.reading_time} min")

with c3:
    st.metric("Sections", len(paper.sections))

with c4:
    st.metric("Chunks", len(paper.chunks))

st.divider()

# ----------------------------
# Analysis Report
# ----------------------------

st.markdown(
    paper.summary if paper.summary else "No analysis generated."
)

# ----------------------------
# Workspace
# ----------------------------

left, right = st.columns([2, 1])

with left:

    st.subheader("Ask Paper")

    render_chat(paper)

    st.subheader("Document Preview")

    preview_text = paper.full_text[:6000]

    if len(paper.full_text) > 6000:
        preview_text += "\n\n...\n\nPreview truncated."

    st.text_area(
        "Preview",
        preview_text,
        height=500,
        disabled=True
    )

with right:

    st.subheader("Paper Information")

    st.write(f"""
**Filename:** {paper.filename}

**Pages:** {paper.pages}

**Reading Time:** {paper.reading_time} min

**Sections:** {len(paper.sections)}

**Chunks:** {len(paper.chunks)}
""")

    st.subheader("Authors")

    if paper.authors:
        for author in paper.authors:
            st.write(author)
    else:
        st.write("No authors detected")

    st.subheader("Actions")

    if st.button("Regenerate Analysis"):

        with st.spinner("Generating..."):

            paper = analysis.generate_all(paper)

            vector.save(paper)

            st.session_state.paper = paper

            st.rerun()

    if st.button("Clear Chat"):

        paper.chat_history = []

        st.session_state.paper = paper

        st.rerun()

# ----------------------------
# Export
# ----------------------------

st.divider()

render_export(paper)