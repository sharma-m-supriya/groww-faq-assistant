import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Groww FAQ Assistant", layout="centered")

# Custom CSS (THIS makes it look like Groww)
st.markdown("""
    <style>
    .main {
        background-color: #f7f9fb;
    }
    .title {
        text-align: center;
        font-size: 48px;
        font-weight: 700;
        color: #2e2e2e;
    }
    .subtitle {
        text-align: center;
        color: gray;
        font-size: 18px;
    }
    .answer-box {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# Navbar
st.markdown("### Groww FAQ Assistant")
st.markdown("**Facts only. No investment advice.**")

# Hero section
st.markdown('<p class="title">Groww your knowledge 📈</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Ask factual mutual fund questions</p>', unsafe_allow_html=True)

st.write("")

# Load data
df = pd.read_csv("data.csv", sep="|")

# User input
query = st.text_input("Ask your question:")

# Example buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("ELSS lock-in"):
        query = "ELSS lock-in period"

with col2:
    if st.button("Exit load"):
        query = "Exit load SBI Bluechip Fund"

with col3:
    if st.button("Minimum SIP"):
        query = "Minimum SIP SBI Flexicap Fund"

# Answer logic
if query:
    result = df[df["question"].str.lower().str.contains(query.lower())]

    if not result.empty:
        answer = result.iloc[0]["answer"]
        source = result.iloc[0]["source"]

        st.markdown(f"""
        <div class="answer-box">
        <b>Answer:</b><br>{answer}<br><br>
        🔗 Source: {source}
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("Sorry, I only answer factual mutual fund questions. No advice.")
