import streamlit as st

from services.export_service import ExportService


exporter = ExportService()


def render_export(paper):

    st.subheader(
        "Export Report"
    )

    try:

        file = exporter.export(
            paper
        )

        with open(
            file,
            "rb"
        ) as pdf:

            st.download_button(

                label="Download Research Report",

                data=pdf,

                file_name=file.split("/")[-1],

                mime="application/pdf"

            )

    except Exception as e:

        st.error(

            f"Export failed: {e}"

        )