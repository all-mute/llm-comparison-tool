import streamlit as st
import requests
import os

st.set_page_config(page_title="Перевод редких языков", layout="wide")
st.title("Перевод редких языков")

# Предполагается, что сервер запущен на localhost:8000
SERVER_URL = "http://studcamp.merkulov.ai"

def get_translation(model_name, prompt):
    endpoint = "/generate_text_big" if "nllb-200" in model_name else "/generate_text_mini"
    data = {"prompt": prompt}
    if "nllb-200" in model_name:
        data["mode"] = model_name.split('-')[-1]
    else:
        data["model_name"] = model_name
    response = requests.post(SERVER_URL + endpoint, json=data)
    return response.json()

def configuration():
    models = [
        'nllb-200-translation_en_to_fr',
        'smallmodel_1'
    ]
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

configuration()

user_input = st.text_area("Enter your request", placeholder="Enter here the user request", height=100)

send_button = st.button("Send Request")

if send_button:
    if not st.session_state.get('selected_models', []):
        st.error("Please select at least one model")
    else:
        if not user_input:
            st.error("Please enter a request")
        else:
            responses = []
            for model in st.session_state.selected_models:
                response = get_translation(model, user_input)
                responses.append((model, response))
            show_response(responses)
