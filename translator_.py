import datetime
import json

import streamlit as st

from llm_handler import *

st.set_page_config(page_title="Перевод редких языков", layout="wide")
st.title("Перевод редких языков")


def configuration():
    models = [
        'bigmodel-translation_en_to_fr',
        'smallmodel_1'
    ]
    cols = st.columns([5, 2, 1])
    with cols[0]:
        st.session_state.models = st.multiselect("Model(s)", models, placeholder="Select one or two models")

    # Models are listed in the order the user selected them
    # Sort the selected list by name to make them easier to find in the results
    st.session_state.models = sorted(st.session_state.models, key=lambda x: x.name)


def show_response(response):
    # Sort the response by model name to keep the order consistent

    # Show the response side by side by model
    cols = st.columns(len(response))
    for i, (m, r) in enumerate(response.items()):
        with cols[i]:
            st.markdown(f"### {m.name}")
            with st.expander("Click to show/hide the raw response"):
                st.write("LLM response data")
                st.write("")

configuration()

user_input = st.text_area("Enter your request", placeholder="Enter here the user request", height=100)

send_button = st.button("Send Request")

if send_button:
    if not st.session_state.models:
        st.error("Please select at least one model")
        st.stop()
    if not user_input:
        st.error("Please enter a request")
        st.stop()

    # Because the download button (below) reruns the entire page (as all of the Streamlit widgets do), we need to
    # save the results in the session state to show them again after the download button is clicked
    # References:
    #  - https://github.com/streamlit/streamlit/issues/3832
    #  - https://discuss.streamlit.io/t/download-button-reloads-app-and-results-output-is-gone-and-need-to-re-run/51467
    models = st.session_state.models
    st.session_state.responses = []

    for model in models:
        str_model = str(model)
        if str_model.startswith('big'):
            mode = str_model.split('-')[1]
            response = get_translation(
                modelname=model,
                mode=mode,
                promt=user_input
            )

            st.session_state.responses.append([str_model, response])

if st.session_state.responses:
    show_response(st.session_state.responses)
