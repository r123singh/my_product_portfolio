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

st.title("👩‍💼 Personal Work Assistant: PWA")
st.markdown("### :rocket: Project Overview")
st.markdown("""
The Personal Assistant is an AI-powered productivity tool that is designed to automate repetitive tasks such as drafting emails, creating study plans, extracting action points from meeting notes, and answering knowledge-based queries. The application leverages advanced language models to provide quick, accurate, and contextual responses.
""")

# Objective
st.markdown("### 🎯 Objective")
st.markdown("""
The primary objective of this project was to:
- The primary goal of the Personal Assistant is to streamline productivity by automating common tasks that knowledge workers and students frequently encounter.
- The app will offer users the ability to:
    - Draft professional emails
    - Create structured study plans
    - Extract actionable insights from text-based content like meeting notes
    - Provide quick answers to user queries based on a knowledge base
                """)

# Key Features
st.markdown("### 📋 Key Features")
st.markdown("""
- **Draft Emails:** Generate polished and professional emails effortlessly.
- **Study Plan Creation:** Create personalized study plans based on your goals and schedule.
- **Extract Action Points:** Automatically identify actionable items from text inputs (e.g., meeting notes).
- **Knowledge-Based Q&A:** Answer questions using internal or provided knowledge bases.
- **Interactive Query Agent:** Submit quick queries through a responsive input agent.
""")

# Impact Made
st.markdown("###  📈 Impact Made")
st.markdown("""
- **Productivity boost** - Increased efficiency and reduced manual effort.
- **Time-saving** - Automate repetitive tasks to free up time for more important work.
- **Improved decision-making** - Access relevant information quickly to make informed choices.
- **Increased efficiency** - Streamline workflows and reduce the time spent on routine tasks.
- **Improved user experience** - Enjoy a user-friendly interface that makes productivity a breeze.
""")

# Value Proposition
st.markdown("### 💡 Value Proposition")
st.markdown("""
The Personal Assistant delivers value by:
- Seamless Email Drafting: Generate polished and professional emails effortlessly.
- Personalized Study Plans: Create personalized study plans based on your goals and schedule.
- Actionable Insights: Automatically identify actionable items from text inputs (e.g., meeting notes).
- Knowledge-Based Q&A: Answer questions using internal or provided knowledge bases.
- Interactive Query Agent: Submit quick queries through a responsive input agent.
- User-Friendly Design: Intuitive interface powered by Streamlit for easy interaction.
""")

# Link to documentation
st.markdown("### 📚 Project Resources")
st.markdown("""
- **[Product Requirements Document (PRD)](https://www.notion.so/AI-based-Personal-Assistant-Application-128161dd646e80dbb23fdeaebefef60c?pvs=4)**
""")

# Screenshots
st.markdown("### 📸 Screenshots")
col1, col2, col3 = st.columns(3)
with col1:
    st.image(Image.open("pages/pwa-project/email.png"), caption="Draft Emails")
with col2:
    st.image(Image.open("pages/pwa-project/kb.png"), caption="Interactive Query Agent")
with col3:
    st.image(Image.open("pages/pwa-project/study.png"), caption="Create Study Plans")

st.markdown("### 🌐 Visit Live Product")
st.markdown("""
Click the button below to experience the Personal Assistant in action.
""")
st.button("Visit Live Product", help="https://personal-assistant-pwa.streamlit.app/")

# Technologies Used
st.markdown("### :bar_chart: Technologies Used")
st.markdown("""
- **Language**: Python  
- **Backend**: OpenAI APIs for Generative AI tasks  
- **LangChain:** Core framework to manage and build language models.
- **Streamlit:** Front-end framework for interactive user interface.
""")
# conclusion
st.markdown("### 📝 Conclusion")
st.markdown("""
The Personal Assistant aims to empower users by providing a simple yet powerful AI-driven solution to automate common tasks. By focusing on ease of use, reliability, and performance, this product is set to enhance productivity for both professionals and students alike.
""")