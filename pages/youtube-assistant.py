import streamlit as st
from PIL import Image
st.set_page_config(page_title="Project Detail", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")

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

st.title("🎥 Youtube Engager")
st.markdown("### :rocket: Project Overview")
st.markdown("""
            In today's fast-paced world, efficiently extracting key information from lengthy YouTube videos can be invaluable. In this project I built a Python application that generates concise summaries of YouTube videos using only their URLs. An AI-powered YouTube Video Summarizer that generates concise summaries and thought-provoking questions from YouTube videos using just their links. This tool is designed to help users quickly understand video content without watching the entire video. """)

# Objective
st.markdown("### 🎯 Objective")
st.markdown("""
The primary objective of this project was to: 
- Build an AI-powered YouTube Video Summarizer that generates concise summaries
- Generate thought-provoking questions from YouTube videos using just their links. 
- Assist users quickly understand video content without watching the entire video.
""")

# Key Features
st.markdown("### 🌟 Key Features")
st.markdown("""
- **Quick Summaries**: Converts long video transcripts into brief and meaningful summaries.
- **User-friendly Interface**: Only requires a YouTube link input to generate a summary.
- **Thought-provoking Questions**: Generates thought-provoking questions from YouTube videos using just their links.
- **Time-Saving**: Provides instant insights into video content, making it useful for decision-making.
- **Seamless YouTube Integration**: Works with YouTube video links to fetch transcripts automatically.
""")


# Value Proposition
st.markdown("### 💡 Value Proposition")
st.markdown("""
The AI powered Youtube Assistant delivers value by:
- **Content Reviewers**: Get quick insights from long videos.
- **Students & Researchers**: Easily digest educational content.
- **Marketers**: Analyze trends or summaries without watching hours of video material
- **Productivity Boost**: Save time and effort by quickly summarizing complex content.
- **User-friendly Interface**: Only requires a YouTube link input to generate a summary.
""")

# Link to documentation
st.markdown("### 📚 Project Resources")
st.markdown("""
- **[Product Requirements Document (PRD)](https://www.notion.so/Youtube-Video-Summarizer-3f4e633afe9c4402b5e40eff91fce76b?pvs=4)**
- **[Dev Posts](https://dev.to/buildandcodewithraman/tldw-summarize-youtube-videos-with-openai-1hb7q)**
""")

# Screenshots
st.markdown("### 📸 Screenshots")
col1, col2, col3 = st.columns(3)
with col1:
    st.image(Image.open("pages/youtube-assistant/home.png"), caption="Home Page")
with col2:
    st.image(Image.open("pages/youtube-assistant/summary.png"), caption="Summary Page")
with col3:
    st.image(Image.open("pages/youtube-assistant/qcreator.png"), caption="Question Creation Page")

st.markdown("### 🌐 Visit Live Product")
st.markdown("""
Click the button below to experience the AI-powered chatbot in action.
""")
st.button("Visit Live Product", help="https://youtube-engage.streamlit.app/")

# Technologies Used
st.markdown("### :bar_chart: Technologies Used")
st.markdown("""
- **Python**: Core programming language for backend processing.
- **Streamlit**: Interactive web interface for ease of use.
- **OpenAI API**: Powers intelligent summarization and question generation.
- **YouTube Transcript API**: Fetches video transcripts for analysis.
""")

# Conclusion
st.markdown("### 🎉 Conclusion")
st.markdown("""
This project demonstrates how to build an AI-powered YouTube Video Summarizer that generates concise summaries and thought-provoking questions from YouTube videos using just their links. This tool is designed to help users quickly understand video content without watching the entire video.
""")

# limitations
st.markdown("### 🚫 Limitations")
st.markdown("""
- - **Transcript Availability**: If the video transcript is unavailable, the application won’t generate a summary.
- **API Usage Limits**: The OpenAI API has usage limits based on the subscription plan.
""")

# Future Work
st.markdown("### 🔮 Future Work")
st.markdown("""
- **Enhanced Summarization**: Implement advanced summarization techniques to improve summary quality.
- **Language Support**: Add support for more languages.
- **User Feedback**: Incorporate user feedback to improve the tool.
""")
