import streamlit as st
from pyvis.network import Network
import requests
import tempfile
import os
from utils import render_footer
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components
from topic_map import generate_topic_timeline
import streamlit_timeline
import json

root_topic = st.session_state["selected_topic"]


st.markdown("---")
st.subheader("📅 Timeline of Topic")

timeline_data = generate_topic_timeline(root_topic)
streamlit_timeline.timeline(json.dumps({"events": timeline_data}), height=600)

timeline_data = generate_topic_timeline(root_topic)

if timeline_data and timeline_data.get("events"):
    streamlit_timeline.timeline(json.dumps(timeline_data), height=600)
else:
    st.info("No timeline data could be extracted for this topic.")
