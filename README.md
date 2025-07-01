# 🌐 Wikitrail  
### *Explore. Learn. Connect.*

---

🎓 **Wikitrail** is a next-generation knowledge dashboard that transforms **any Wikipedia topic** into an immersive, AI-powered **learning universe**.  
From concept maps and contributor cards to personalized quizzes and forums — it’s where curiosity meets cutting-edge tech.

---

## ✨ What Makes Wikitrail Unique?

| 🌟 Feature | 🎯 Purpose |
|------------|------------|
| **AI Chatbot** | Context-aware tutor that grows with your topic |
| **Concept Maps** | See knowledge as a web, not a wall |
| **Timelines** | Travel through time and discovery |
| **Forums** | Build mini-communities around shared interests |
| **Contributor Cards** | Meet the legends behind the knowledge |
| **Quizzes** | Learn actively, track your progress |
| **Books & Films** | Dive deeper with curated media |

---

## 🧭 Explore the Trail: Page-by-Page

### 🔍 Home Page
- 📚 Search any topic — **text or voice**
- 🌐 Toggle between **Indic & Global languages**
- 🎙️ Multilingual speech input via Bhashini / IndicNLP

---

### 📖 Page 1: Summary + Deep Dive
- 🧠 Wikipedia-enhanced overview
- 🧬 Interactive advanced topics (click to expand)
- 🤖 Persistent AI tutor — explain like I’m 12? You got it.

---

### 🧠 Page 2: Concept Map + Timeline
- 🌌 Zoomable, explorable **knowledge graph**
- 🕰️ Interactive timeline of breakthroughs & historical moments

---

### 💬 Page 3: Community Forums
- 🗣️ Topic-focused spaces to:
  - Ask questions  
  - Share resources  
  - Discuss ideas  
- 🔒 Encourages focused, distraction-free learning

---

### 🧑‍🏫 Page 4: Contributors
- 🧲 Beautiful **PluckCards** of scientists, historians, pioneers
- 🖱️ Hover = bio preview  
- 🔄 Click = new search trail with their name

---

### 🎥 Page 5: Books & Movies
- 📚 Curated reads and documentaries  
- 🎬 Clean, card-style layout  
- ❌ No ads. No purchases. Just pure discovery

---

### 🧩 Page 6: Quiz & Tracker
- 🧪 AI-generated quizzes — by difficulty level  
- 🧮 Score saved *per topic* in browser (no login required)  
- 🏅 Track growth and return later for mastery

---

### 🤖 Persistent AI Chatbot
- 🧙 Choose a **persona**: Einstein, Historian, Kid-friendly  
- 🔒 Strictly contextual — answers only about your current topic  
- 🎯 Fast, smart, and always by your side

---

## 🧠 Powered By

| Layer      | Technologies |
|------------|--------------|
| Frontend   | `Streamlit` (MVP), `React` (for UI scaling) |
| Backend    | `FastAPI`, `Python` |
| AI/NLP     | `OpenAI GPT`, `LangChain`, `Sentence Transformers` |
| Data APIs  | `MediaWiki`, `Wikidata`, `Google Books`, `Arxiv`, `Reddit` |
| Graphs/UI  | `pyvis`, `D3.js`, `Altair`, `TailwindCSS` |
| Voice/Indic | `SpeechRecognition`, `IndicTrans`, `Bhashini`, `gTTS` |
| Storage    | `LocalStorage`, `IndexedDB` |

---

## 🌍 Language Support

🌐 **Toggle interface and content language**  
🗣️ Translate summaries, quizzes & chat using AI  
📣 Optional **Indic language support** for search, speech, and display

---

## 🧪 Getting Started (Streamlit MVP)

```bash
git clone https://github.com/yourusername/wikiverse-pro.git
cd wikiverse-pro
pip install -r requirements.txt
streamlit run app.py

## 📁 Project Structure

```plaintext
wikiverse_pro/
├── app.py               # 🔑 Main app with navigation
├── pages/               # 🗂️ Multi-page modules
│   ├── 1_Basic_Info.py   # 📄 Basic info
│   ├── 2_Topic_Map.py    # 🗺️ Topic map
│   ├── 3_Forums.py       # 💬 Forums
│   ├── 4_Contributors.py # 👥 Contributors
│   ├── 5_Books_Movies.py # 📚 Books & movies
│   └── 6_Quiz.py         # ❓ Quiz
├── utils.py             # 🤖 Chatbot + utilities
├── requirements.txt     # 📦 Dependencies
└── README.md            # 📄 Docs
