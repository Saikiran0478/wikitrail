# utils.py
import requests
import streamlit as st

HUGGINGFACE_API_TOKEN = "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"  # ✅ use your working token

CHAT_MODEL_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}


def query_chatbot(prompt):
    payload = {"inputs": prompt}
    try:
        response = requests.post(CHAT_MODEL_URL, headers=HEADERS, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()[0]["generated_text"]
    except Exception as e:
        return f"Error: {str(e)}"

def generate_advanced_info(summary):
    prompt = f"""
    You're an expert teacher. Expand this summary of a topic:
    
    Summary: {summary}
    
    Return in this format:
    - Key Subtopics
    - Definitions
    - Real-world Applications
    - Background
    """
    return query_chatbot(prompt)

def render_chatbot():
    st.sidebar.markdown("### 🤖 Ask the WikiBot")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.sidebar.text_input("You:", key="chat_input")

    if user_input:
        response = query_chatbot(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))

    for role, msg in st.session_state.chat_history[::-1]:
        with st.sidebar.chat_message(role):
            st.markdown(msg)
