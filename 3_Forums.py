import streamlit as st
import requests
from urllib.parse import quote_plus
from utils import render_footer, render_chatbot

st.set_page_config(page_title="💬 Forums & Discussions", layout="wide")
st.title("💬 Forums & Community Discussions")

if "selected_topic" not in st.session_state:
    st.warning("⚠️ No topic selected. Please go to the homepage and enter a topic.")
    st.stop()

topic = st.session_state["selected_topic"]
encoded = quote_plus(topic)

st.success(f"🔍 Community discussions and resources for: **{topic}**")
st.markdown("---")

# 🎯 General search engines and Q&A platforms
platforms = {
    "Reddit": {
        "url": f"https://www.reddit.com/search/?q={encoded}",
        "icon": "https://upload.wikimedia.org/wikipedia/en/thumb/1/1f/Reddit_logo_2023.svg/768px-Reddit_logo_2023.svg.png"
    },
    "YouTube": {
        "url": f"https://www.youtube.com/results?search_query={encoded}+explanation+discussion",
        "icon": "https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg"
    },
    "Quora": {
        "url": f"https://www.quora.com/search?q={encoded}",
        "icon": "https://download.logo.wine/logo/Quora/Quora-Logo.wine.png"
    },
    "Stack Exchange": {
        "url": f"https://stackexchange.com/search?q={encoded}",
        "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Stack_Exchange_logo_and_wordmark.svg/1200px-Stack_Exchange_logo_and_wordmark.svg.png"
    },
    "Wikipedia Talk": {
        "url": f"https://en.wikipedia.org/wiki/Talk:{encoded.replace(' ', '_')}",
        "icon": "https://upload.wikimedia.org/wikipedia/commons/8/80/Wikipedia-logo-v2.svg"
    },
    "Google Forums": {
        "url": f"https://groups.google.com/g/{encoded}",
        "icon": "https://upload.wikimedia.org/wikipedia/commons/5/5a/Google_Groups_logo.png"
    }
}

# 🖼️ Display platform cards
cols = st.columns(3)
for i, (name, data) in enumerate(platforms.items()):
    with cols[i % 3]:
        st.markdown(f"""
        <div style="text-align: center;">
            <a href="{data['url']}" target="_blank">
                <img src="{data['icon']}" width="80" />
                <div style="margin-top: 0.5rem; font-weight: bold; color: white;">{name}</div>
            </a>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.subheader("🤖 Chat with WikiBot")
render_chatbot(topic)

render_footer()

# 🔁 Navigation Buttons
col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    if st.button("⬅️ Previous"):
        st.switch_page("pages/2_Concept_Mapping.py")

with col3:
    if st.button("Next ➡️"):
        st.switch_page("pages/4_Give_Review_Here.py")

with col2:
    if st.button("🔁 New Search"):
        for key in ["selected_topic"]:
            st.session_state.pop(key, None)
        st.switch_page("Home.py")
