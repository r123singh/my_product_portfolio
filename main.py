import streamlit as st 
from PIL import Image 
st.set_page_config(page_title="Product Management Portfolio", page_icon="🚀", layout="wide", initial_sidebar_state="collapsed")

# Set dark theme for the entire application
st.markdown("""
    <style>
    /* Main app background */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Text color */
    body {
        color: #FAFAFA;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #0E1117;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #FAFAFA !important;
    }
    
    /* Paragraphs */
    p {
        color: #FAFAFA !important;
    }
    
    /* Links */
    a {
        color: #00B4D8 !important;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #00B4D8;
        color: #0E1117;
    }
    
    .stButton>button:hover {
        background-color: #0077B6;
        color: #FAFAFA;
    }
    
    /* Input fields */
    .stTextInput>div>div>input {
        background-color: #262730;
        color: #FAFAFA;
    }
    
    /* Select boxes */
    .stSelectbox>div>div>select {
        background-color: #262730;
        color: #FAFAFA;
    }
    
    /* Slider */
    .stSlider>div>div>div {
        background-color: #00B4D8;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .stApp{
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
    unsafe_allow_html=True,
)

col1, col2 = st.columns([1,3])

with col1:
    profile_image = Image.open("profile.jpeg")
    st.markdown("""
        <style>
        img {
            pointer-events: none;
            -webkit-user-select: none;
            -ms-user-select: none;
            user-select: none;
        }
        </style>
        """, unsafe_allow_html=True)
    st.image(profile_image, width=150)
    
with col2:
    st.title("Ramandeep Singh")
    st.subheader("Product Manager | AI Enthusiast | Tech Innovator | SaaS Expert")
    
st.markdown("### 🚀Key Highlights")
st.markdown(
    """
    - **10+ Years** of experience in tech product industry working with startups and large companies.
    - **5+ Years** in AI-driven product development building products that drive user engagement and business growth.
    - **3 Successful Product Launches** with over 1M users, 100K+ downloads and 100K+ active users.
    - **Certified Scrum Master** & **Agile Practitioner** created and managed agile teams to deliver products on time and within budget.
    - **SaaS Expert** with a deep understanding of the SaaS business model and the challenges of building a successful SaaS company.
    """)

st.markdown("### 📝 Summary")
st.markdown(
    """
    I am a passionate Product Manager with a strong background in AI and machine learning. I have a proven track record of delivering innovative products that drive user engagement and business growth. My expertise lies in bridging the gap between technical teams and business stakholders to create products that are both technically sound and market-ready.
    """
)   

st.markdown("### 🛠️ Key Skills")
st.markdown(
    """
    - **Product Strategy & Roadmapping**
    - **Agile & Scrum Methodologies**
    - **Data-Driven Decision Making**
    - **User Experience (UX) Design**
    - **AI & Machine Learning Integration**
    - **Stakeholder Management**
    """
)

st.markdown("### 🚀 Projects")

col1, col2 = st.columns([1,3])

with col1:
    project0_image = Image.open("pages/speech-assistant/thumbnail.png")
    st.image(project0_image, width=150)

with col2:
    st.markdown("#### Smart Meeting Assistant")
    st.markdown(
    """
    Built a scalable AI-powered platform leveraging OpenAI, Python. Integrated features include audio transcription, MoM generation, sentiment analysis, and multilingual support. Access control was implemented via Gumroad API for monetization.  To enable seamless audio-to-text conversion, multilingual transcription, and automated meeting summaries, empowering users with efficient communication tools.
    """
    )
    if st.button("Visit Project", key="speech-assistant-btn"):
        st.switch_page("pages/speech-assistant.py")
col1, col2 = st.columns([1,3])

with col1:
    project1_image = Image.open("pages/chatbot-project/thumbnail.webp")
    st.image(project1_image, width=150)

with col2:
    st.markdown("#### GenAI-Powered Chatbot")
    st.markdown(
    """
    Developed an AI-powered chatbot for customer support, reducing response time by 40%. Integration with NLP and machine learning models for better understanding and response accuracy
    """
    )
    if st.button("Visit Project", key="chatbot-project-btn"):
        st.switch_page("pages/chatbot-project.py")

col1, col2 = st.columns([1,3])

with col1:
    project1_image = Image.open("pages/pwa-project/thumbnail.webp")
    st.image(project1_image, width=150)

with col2:
    st.markdown("#### Personal Work Assistant")
    st.markdown(
    """
    Developed a Personal Work Assistant that helps users manage their work and schedule. It uses generative AI models to help users with their work and schedule.Plan creation, email drafting, and query answering.
    """
    )
    if st.button("Visit Project", key="pwa-project-btn"):
        st.switch_page("pages/pwa-project.py")


col1, col2 = st.columns([1,3])

with col1:
    project2_image = Image.open("pages/stock-recommender/thumbnail.webp")
    st.image(project2_image, width=150)

with col2:
    st.markdown("#### Stock Recommender")
    st.markdown(
    """
    Built a stock recommender that helps investors choose the best stocks to buy from a provided list, based on their risk tolerance, investment horizon, and goals. Shown live stock data in real-time.
    """
    )
    if st.button("Visit Project", key="stock-recommender-btn"):
        st.switch_page("pages/stock-recommender.py")
    

col1, col2= st.columns([1,3])

with col1:
    project3_image = Image.open("pages/youtube-assistant/thumbnail.webp")
    st.image(project3_image, width=150)

with col2:
    st.markdown("#### Youtube Video Assistant")
    st.markdown(
    """
    Created a Youtube Video Summarizer that generates concise summaries and thought-provoking questions from YouTube videos using just their links. This tool is designed to help users quickly understand video content without watching the entire video. Long videos can be a pain to watch, and this tool is designed to help users quickly understand the video content without watching the entire video.
    """
    )
    if st.button("Visit Project", key="youtube-assistant-btn"):
        st.switch_page("pages/youtube-assistant.py")
    
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0E1117, #1E1E2F, #2E2E4F);
        background-size: 200% 200%;
        animaton: gradient 15s ease infinite;
    }
    
    @keyframes gradient {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)
