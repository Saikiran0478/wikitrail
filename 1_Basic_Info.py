# pages/1_Basic_Info.py

import streamlit as st
import requests
from utils import render_chatbot, generate_advanced_info


st.set_page_config(
    page_title="Basic Info - WikiVerse Pro",
    page_icon="📖",
    layout="wide",
)

render_chatbot()  # Keep chatbot on sidebar

# Topic state check
if "selected_topic" not in st.session_state:
    st.warning("Please go back to the homepage and enter a topic.")
    st.stop()

topic = st.session_state["selected_topic"]
language = st.session_state.get("language", "English")

st.title(f"📖 Basic Info: {topic}")
st.caption(f"🔤 Language: {language}")

# --- Wikipedia API Call ---
def get_summary(topic, lang="en"):
    try:
        url = f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{topic.replace(' ', '_')}"
        response = requests.get(url)
        if response.status_code == 404:
            return topic, f"❗ This topic is not available in {lang}. Try searching in English.", None
        response.raise_for_status()
        data = response.json()
        return data.get("title", topic), data.get("extract", "No summary available."), data.get("thumbnail", {}).get("source", None)
    except Exception as e:
        return topic, f"Error retrieving summary: {e}", None

# Language code mapping (for Wikipedia API)
lang_map = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn"
}
wiki_lang = lang_map.get(language, "en")

title, summary, image = get_summary(topic, lang=wiki_lang)

# --- Display Summary ---
col1, col2 = st.columns([2, 1])
with col1:
    st.subheader(title)
    st.write(summary)

with col2:
    if image:
        st.image(image, width=300)
    else:
        st.info("No image available.")

# --- Expandable Advanced Info ---
with st.expander("📘 Show Advanced Information"):
    # Optional placeholder until you add NLP-based advanced content
    st.markdown("""
    - This section can include:
        - Subtopics
        - Technical definitions
        - Key figures & equations
        - Real-world applications
    - Use NLP or GPT to enrich this with AI-based summaries.
    """)

# Navigation option to next page
if st.button("Next ➡️ Concept Map"):
    st.switch_page("pages/2_Topic_Map.py")

# --- Expandable Advanced Info (AI-enhanced) ---
with st.expander("📘 Show Advanced Information"):
    st.markdown("Generating deeper insights using AI...")

    if "advanced_info" not in st.session_state:
        with st.spinner("Analyzing the topic..."):
            st.session_state.advanced_info = generate_advanced_info(summary)

    st.markdown(st.session_state.advanced_info)
