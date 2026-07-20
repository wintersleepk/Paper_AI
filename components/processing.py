import streamlit as st
import time


def render_processing():

    steps = [

        "Reading document",

        "Extracting content",

        "Generating embeddings",

        "Building vector database",

        "Generating AI analysis",

        "Preparing workspace"

    ]

    progress = st.progress(0)

    status = st.empty()

    total = len(steps)

    for index, step in enumerate(steps):

        status.info(step)

        progress.progress(

            int(

                (index + 1)
                / total
                * 100

            )

        )

        time.sleep(0.15)

    status.success(

        "Processing complete"

    )

    time.sleep(0.3)

    progress.empty()

    status.empty()