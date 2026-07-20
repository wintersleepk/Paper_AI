import streamlit as st


def metric_card(title, value):

    st.metric(

        label=title,

        value=value

    )


def section_card(title, content):

    st.subheader(title)

    st.markdown(

        content if content else "No content available."

    )


def info_card(label, value):

    st.write(

        f"**{label}:** {value}"

    )


def status_card(status):

    if status == "Ready":

        st.success(status)

    else:

        st.error(status)