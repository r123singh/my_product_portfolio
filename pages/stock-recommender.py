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

st.title(":chart_with_upwards_trend: Stocks Recommender Engine")
st.markdown("### :rocket: Project Overview")
st.markdown("""
Invest smarter with our AI-Powered Stock Recommender! This version helps you analyze market trends, track real-time stock data, and get AI-driven insights. 📊🤖. Built a stocks recommender engine that uses generative AI models to recommend stocks to the user based on their risk tolerance and investment goals.
""")

# Objective
st.markdown("### 🎯 Objective")
st.markdown("""
The primary objective of this project was to:
- Guide new market entrants with limited budgets choose the best stocks to buy from a provided list, based on their risk tolerance, investment horizon, and goals.
- Provide a simple and easy-to-use interface for users to get stock recommendations.
- Use generative AI models to recommend stocks to the user based on their risk tolerance and investment goals.
""")

# Key Features
st.markdown("### 🌟 Key Features")
st.markdown("""
✅ Real-Time Stock Data Fetching – Use APIs like Yahoo Finance, Alpha Vantage, or Finnhub to get live stock prices and trends.
✅ Personalized Recommendations – Tailor stock suggestions based on risk tolerance, budget, and investment goals.
✅ Portfolio Simulation – Allow users to create a virtual portfolio and track potential gains/losses.
✅ Sector-Based Filtering – Let users filter stocks by Technology, Healthcare, EV, Consumer Goods, etc.
✅ Dividend vs. Growth Stock Comparison – Show which stocks offer consistent dividends vs. high growth potential.
""")

# Impact Made
st.markdown("###  📈 Impact Made")
st.markdown("""
- **Helped new market entrants choose the best stocks to buy from a provided list, based on their risk tolerance, investment horizon, and goals.**
- **Provided a simple and easy-to-use interface for users to get stock recommendations.**
- **Used generative AI models to recommend stocks to the user based on their risk tolerance and investment goals.**
""")

# Value Proposition
st.markdown("### 💡 Value Proposition")
st.markdown("""
The AI powered Stock Recommender delivers value by:
- Providing instant stock recommendations based on the user's risk tolerance and investment goals.
- Helping users save time and money by not having to research and analyze stocks.
- Providing a simple and easy-to-use interface for users to get stock recommendations.
   - ✅ Fetch live stock prices from Yahoo Finance
   - ✅ User input for multiple stocks
   - ✅ Display stock price changes in real-time
   - ✅ Interactive UI
""")

# Link to documentation
st.markdown("### 📚 Project Resources")
st.markdown("""
- **[Product Requirements Document (PRD)](https://www.notion.so/Stock-Recommender-Product-Requirements-Document-PRD-1a6161dd646e8062affdcf1af5ad8fc9?pvs=4)**
- **[Flowcharts](https://www.notion.so/Stock-Tracker-Roadmap-1a6161dd646e8075bce4ddec4fea5b24?pvs=4)**
- **[Project Timeline](https://www.notion.so/Stock-Tracker-Roadmap-1a6161dd646e8075bce4ddec4fea5b24?pvs=4)**
""")

# Screenshots
st.markdown("### 📸 Screenshots")
col1, col2, col3 = st.columns(3)
with col1:
    st.image(Image.open("pages/stock-recommender/landing.png"), caption="Investor Landing")
with col2:
    st.image(Image.open("pages/stock-recommender/options.png"), caption="Options Dashboard")
with col3:
    st.image(Image.open("pages/stock-recommender/livedata.png"), caption="Live Data")

st.markdown("### 🌐 Visit Live Product")
st.markdown("""
Click the button below to experience the AI-powered chatbot in action.
""")
st.button("Visit Live Product", help="https://stocks-basix.streamlit.app/")

# Technologies Used
st.markdown("### :bar_chart: Technologies Used")
st.markdown("""
- **Frontend**: Streamlit
- **Backend**: Python
- **AI Model**: OpenAI API (GPT-based recommendations)
- **Data Sources**: Yahoo Finance, Alpha Vantage, or other market data APIs
""")

# Future Enhancements
st.markdown("### 🔮 Future Enhancements")
st.markdown("""
- ✅ Implement portfolio tracking.
- ✅ Add more advanced AI models for better predictions.
- ✅ Enhance UI with interactive visualizations.
- ✅ Support multiple stock exchanges.
- ✅ Add more features like portfolio simulation, sector-based filtering, and dividend vs. growth stock comparison. 
""")

