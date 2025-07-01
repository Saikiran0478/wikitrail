# topic_map.py
import requests
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components
import tempfile

# 🔌 Replace with your Hugging Face token (or use OpenAI if preferred)
HUGGINGFACE_API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}


# 📘 Fetch related topics from Wikipedia
import requests
from pyvis.network import Network
import streamlit as st
import tempfile
import streamlit.components.v1 as components


# 📥 Get related topics dynamically from Wikipedia
def fetch_related_topics(query):
    try:
        search_url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "format": "json",
            "generator": "search",
            "gsrsearch": f"related to {query}",
            "gsrlimit": 10
        }
        response = requests.get(search_url, params=params)
        pages = response.json().get("query", {}).get("pages", {})
        related_titles = [page["title"] for page in pages.values()]
        return related_titles
    except Exception as e:
        print(f"❌ Error: {e}")
        return []


# 🧠 Build the interactive concept graph
def build_topic_graph(root_topic, related_topics):
    net = Network(height="600px", width="100%", bgcolor="#222222", font_color="white")
    net.add_node(root_topic, label=root_topic, color="red")

    for topic in related_topics:
        net.add_node(topic, label=topic, color="skyblue")
        net.add_edge(root_topic, topic)

    return net


# 🌐 Render the graph using PyVis and Streamlit
def render_graph(net):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp_file:
        net.save_graph(tmp_file.name)
        components.html(open(tmp_file.name, 'r', encoding='utf-8').read(), height=650, scrolling=True)

def build_topic_branch_graph(root_topic, related_topics):
    net = Network(height="600px", width="100%", bgcolor="#222222", font_color="white", directed=True)
    
    net.add_node(root_topic, label=root_topic, color="red", size=30)

    for topic in related_topics:
        net.add_node(topic, label=topic, color="skyblue", size=20)
        net.add_edge(root_topic, topic)

    return net