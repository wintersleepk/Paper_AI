import streamlit as st

from utils.styles import load_css
from components.hero import render_hero
from components.uploader import render_uploader
from components.processing import render_processing
from services.pipeline_service import PipelineService


st.set_page_config(
    page_title="PaperMind AI",
    page_icon="assets/logo.png",
    layout="wide"
)

load_css()

if "paper" not in st.session_state:
    st.session_state.paper = None

if "processing_complete" not in st.session_state:
    st.session_state.processing_complete = False


pipeline = PipelineService()


render_hero()

uploaded_file = render_uploader()


if uploaded_file and not st.session_state.processing_complete:

    try:

        render_processing()

        paper = pipeline.process(uploaded_file)

        st.session_state.paper = paper

        st.session_state.processing_complete = True

        st.switch_page("pages/dashboard.py")

    except Exception as e:

        st.error(f"Processing failed: {e}")

        st.session_state.processing_complete = False