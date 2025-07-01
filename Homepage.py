# app.py
import streamlit as st
from utils import render_chatbot

st.set_page_config(
    page_title="Wikitrail",
    page_icon="🌐",
    layout="wide",
)


render_chatbot()  # Sidebar chatbot

st.title("🌐 WikiVerse Pro")
st.markdown("#### Explore. Learn. Connect.")
st.write("Enter a topic to begin your knowledge journey.")

# Indic language option (optional for now)
language = st.selectbox("Choose language for results", ["English", "Hindi", "Telugu", "Tamil", "Kannada"])

# Topic input
topic = st.text_input("🔍 Search Wikipedia Topic", placeholder="e.g., Quantum Computing")

# Optional: voice input (in future)
st.caption("🎙️ Voice search and Indic typing support coming soon!")

if st.button("Explore"):
    if topic:
        # Redirect to first page (you will handle topic routing via session_state)
        st.session_state["selected_topic"] = topic
        st.session_state["language"] = language
        st.switch_page("pages/1_Basic_Info.py")  # Streamlit 1.25+ feature
    else:
        st.warning("Please enter a topic to explore.")
