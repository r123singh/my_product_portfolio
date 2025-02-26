import streamlit as st
from PIL import Image
st.set_page_config(page_title="Project Detail", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
     .css-1d391kg {
        background-color: #0E1117;
    }
    .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3, .css-1d391kg h4, .css-1d391kg h5, .css-1d391kg h6 {
        color: #FAFAFA;
    }
    .css-1d391kg p {
        color: #FAFAFA;
    }
    .css-1d391kg a {
        color: #00B4D8;
    }
    .css-1d391kg .stButton button {
        background-color: #00B4D8;
        color: #0E1117;
    }
    .css-1d391kg .stButton button:hover {
        background-color: #0077B6;
        color: #FAFAFA;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎤 Speech Assistant: AI-Powered Audio-to-Text & MoM Generator")
st.markdown("### :rocket: Project Overview")
st.markdown("""
Meetings are essential for collaboration, but managing their outcomes can be time-consuming. Transcribing conversations, summarizing key points, and tracking action items often demand manual effort. Speech Assistant was created to bridge this gap using cutting-edge AI technology, simplifying and automating meeting management for professionals and organizations.
""")

# Objective
st.markdown("### 🎯 Objective")
st.markdown("""
The primary objective of this project was to:
- Develop a speech-to-text transcription system that accurately converts spoken language into text.
- Create a meeting minutes generator that summarizes key points and action items from audio recordings.
- Implement a user-friendly interface for managing and analyzing meeting transcripts.
- Provide a seamless and efficient solution for meeting management, reducing manual effort and improving productivity.
            """)
# Key Features
st.markdown("### 🌟 Key Features")
st.markdown("""
- 🎙️ **Audio-to-Text Conversion**: Convert meetings, call recordings, and other audio files into text in multiple languages.  
- 🔁 **Text-to-Audio**: Convert text back into audio in any language.  
- 📝 **Minutes of Meeting Generator**: Automatically generate MoM for your audio recordings, including:  
    - Call Sentiments Analysis - Positive, Negative, Neutral
    - Key Points - Key points from the call
    - Summaries - Summary of the call
    - Action Points - Action points from the call
- 📥 **Download Options**: Export MoM as a downloadable file for easy sharing.  
- 🌍 **Multilingual Support**: Handle multiple languages for both audio and text. 
- 📊 **Analytics**: Analyze call sentiments, key points, and action items to improve meeting outcomes.
""")

# Impact Made
st.markdown("###  📈 Impact Made")
st.markdown("""
- 10x Productivity Boost: Speeds up transcription and MoM creation, saving hours of manual work.
- Enhanced Accessibility: Multilingual support ensures inclusivity for global teams.
- Improved Decision-Making: Provides actionable insights and sentiment analysis to drive better outcomes.
""")

# Value Proposition
st.markdown("### 💡 Value Proposition")
st.markdown("""
The AI powered Speech Assistant delivers value by:
- Seamless Audio-to-Text Conversion: Supports various audio formats with high accuracy.
- Automated Minutes of Meeting: Generates summaries, key points, action items, and sentiment insights.
- Multilingual & Bidirectional Support: Converts audio to text and text to audio in multiple languages.
- User-Friendly Design: Intuitive interface powered by Streamlit for easy interaction.
- Downloadable Outputs: Export MoMs and transcriptions for easy sharing and collaboration.
""")

# Link to documentation
st.markdown("### 📚 Project Resources")
st.markdown("""
- **[Product Requirements Document (PRD)](https://www.notion.so/Product-description-167161dd646e80f29fe5cf0fa78c9ac6?pvs=4)**
- **[Revenue Model](https://www.notion.so/Revenue-Generating-Feature-Freemium-Model-with-Paid-Premium-Features-168161dd646e80b38facc1dd2c5bb676?pvs=4)**
- **[Future Enhancements](https://www.notion.so/Future-Enhancements-167161dd646e80c6bf07ef47f56de882?pvs=4)**
""")

# Screenshots
st.markdown("### 📸 Screenshots")
col1, col2, col3 = st.columns(3)
with col1:
    st.image(Image.open("pages/speech-assistant/mom.png"), caption="Minutes of Meeting Generator")
with col2:
    st.image(Image.open("pages/speech-assistant/tts.png"), caption="Text-to-Audio Conversion")
with col3:
    st.image(Image.open("pages/speech-assistant/stt.png"), caption="Audio-to-Text Output")

st.markdown("### 🌐 Visit Live Product")
st.markdown("""
Click the button below to experience the AI-powered Speech Assistant in action.
""")
st.button("Visit Live Product", help="https://smart-meeting-assistant.streamlit.app/")

# Technologies Used
st.markdown("### :bar_chart: Technologies Used")
st.markdown("""
- **Language**: Python  
- **Frontend**: Streamlit  
- **Backend**: OpenAI APIs for Generative AI tasks  
- **Libraries**:  
  - Speech-to-text: OpenAI Whisper  
  - Text-to-speech: Google TTS / Pyttsx3  
  - Sentiment Analysis: VADER, OpenAI GPT  
  - File Handling: Pandas, OS  
""")

# Future Extensions
st.markdown("### 🔮 Future Extensions")
st.markdown("""
- Enable real-time audio-to-text conversion for live meetings, webinars, or calls.
- Integrate with popular platforms like Zoom, Microsoft Teams, or Google Meet to fetch recordings directly.
- Add customizable summarization options (e.g., concise summaries, detailed summaries, or action-only points).
- Provide detailed visualizations of sentiment trends.
""")