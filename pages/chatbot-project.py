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

st.title("📊 AI-Powered Chatbot")
st.markdown("### :rocket: Project Overview")
st.markdown("""
In today’s digital landscape, customers expect seamless, instant, and personalized support whenever they interact with businesses online. To meet these demands, I developed an GenAI-powered chatbot for customer support, reducing response time by 40%. Integration with GenAI models like Claude and Anthropic for better understanding and response accuracy. 
""")

# Objective
st.markdown("### 🎯 Objective")
st.markdown("""
The primary objective of this project was to:
- Reduce customer support response time by 40%
- Improve response accuracy and customer satisfaction using GenAI
- Enhance customer satisfaction and engagement 
            """)
# Key Features
st.markdown("### 🌟 Key Features")
st.markdown("""
- **Multi-modal chatbot interface:** (text, image, video)
- **NLP-based intent recognition and response generation**
- **Machine Learning Integration:** Machine learning models for advanced analytics
- **Multi-Channel Support:** Available on web, mobile, and social media platforms.

""")

# Impact Made
st.markdown("###  📈 Impact Made")
st.markdown("""
- **40% Reduction in Response Time:** Customers receive faster support, leading to higher satisfaction.
- **25% Increase in Customer Engagement:** Personalized responses drive higher engagement.
- **30% Cost Savings:** Reduced dependency on human support agents.
""")

# Value Proposition
st.markdown("### 💡 Value Proposition")
st.markdown("""
The AI powered Chatbot delivers value by:
- Providing instant, accurate, and personalized responses to customer queries.
- Reducing operational costs by automating repetitive tasks.
- Enhancing customer experience through seamless and efficient support.
""")

# Link to documentation
st.markdown("### 📚 Project Resources")
st.markdown("""
- **[Product Requirements Document (PRD)](https://www.notion.so/Convo-Expert-Chatbot-114161dd646e807d879dc112d309cf48?pvs=4)**
- **[Dev Post](https://dev.to/buildandcodewithraman/building-a-chatgpt-lookalike-with-streamlit-and-anthropic-api-46fd)**
- **[Project Demo](https://youtu.be/_nUD-DeBMxQ)**
""")

# Screenshots
st.markdown("### 📸 Screenshots")
col1, col2, col3 = st.columns(3)
with col1:
    st.image(Image.open("pages/chatbot-project/screenshot1.png"), caption="Chatbot Interface")
with col2:
    st.image(Image.open("pages/chatbot-project/screenshot2.png"), caption="Analytics Dashboard")
with col3:
    st.image(Image.open("pages/chatbot-project/screenshot3.png"), caption="Admin Panel")

st.markdown("### 🌐 Visit Live Product")
st.markdown("""
Click the button below to experience the AI-powered chatbot in action.
""")
st.button("Visit Live Product", help="https://chatbot.com")

# Technologies Used
st.markdown("### :bar_chart: Technologies Used")
st.markdown("""
- Python
- Streamlit
- Langchain
- Anthropic API
""")