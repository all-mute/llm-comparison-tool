import streamlit as st
import requests
import os
from llm_handler import get_translation

st.set_page_config(page_title="Перевод редких языков", layout="wide")
st.title("Перевод редких языков")

# Предполагается, что сервер запущен на localhost:8000
SERVER_URL = "http://studcamp.merkulov.ai"

def configuration():
    model_names_0 = [
        'ourmodel_eng_to_lij',
        'ourmodel_eng_to_dik',
        'ourmodel_eng_to_ace',
        'ourmodel_eng_to_mag',
    ]
    model_names_1 = [
        'nllb-200-eng_to_lij',
        'nllb-200-eng_to_dik',
        'nllb-200-eng_to_ace',
        'nllb-200-eng_to_mag',
    ]

    models = model_names_0 + model_names_1

    cols = st.columns([5, 2, 1])
    with cols[0]:
        selected_models = st.multiselect("Model(s)", models, placeholder="Select one or two models")
        st.session_state.selected_models = selected_models

def show_response(response):
    cols = st.columns(len(response))
    for i, (m, r) in enumerate(response):
        with cols[i]:
            st.markdown(f"### {m}")
            with st.expander("Click to show/hide the raw response"):
                st.write(r)
                st.write(r["generated_text"])
            st.info(r["generated_text"])

configuration()

user_input = st.text_area("Enter your request", value="Let's go to france and see the eiffel tower", placeholder="Enter here the user request", height=100)

send_button = st.button("Send Request")

if send_button:
    if not st.session_state.get('selected_models', []):
        st.error("Please select at least one model")
    else:
        if not user_input:
            st.error("Please enter a request")
        else:
            with st.spinner('Processing (CPU)...'):
                responses = []
                for model in st.session_state.selected_models:
                    response = get_translation(model, user_input)
                    responses.append((model, response))
                show_response(responses)
