import streamlit as st
import pandas as pd

# Page config
st.set_page_config(layout="wide")

# 🔥 Groww-style CSS (major upgrade)
st.markdown("""
<style>

body {
    background-color: #F7F9FB;
}

/* Navbar */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 40px;
    background-color: white;
    border-bottom: 1px solid #eee;
}

.logo {
    font-size: 22px;
    font-weight: 700;
    color: #2E2E2E;
}

.menu {
    color: #6b7280;
    font-size: 14px;
}

/* Hero Section */
.hero {
    text-align: center;
    margin-top: 60px;
}

.hero-title {
    font-size: 72px;
    font-weight: 800;
    color: #2E2E2E;
}

.hero-btn {
    background-color: #00D09C;
    color: white;
    padding: 14px 32px;
    border-radius: 30px;
    font-weight: 600;
    display: inline-block;
    margin-top: 20px;
}

/* Input */
.stTextInput > div > div > input {
    border-radius: 30px;
    padding: 12px;
}

/* Answer Card */
.answer-box {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.05);
    margin-top: 30px;
}

/* Buttons */
.stButton>button {
    border-radius: 20px;
    border: 1px solid #00D09C;
    color: #00D09C;
}

.stButton>button:hover {
    background-color: #00D09C;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# 🧭 Navbar
st.markdown("""
<div class="navbar">
    <div class="logo">Groww</div>
    <div class="menu">Facts only • No advice</div>
</div>
""", unsafe_allow_html=True)

# 🎯 Hero Section
st.markdown("""
<div class="hero">
    <div class="hero-title">Groww your wealth</div>
    <div class="hero-btn">Get started</div>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# 📂 Load data
df = pd.read_csv("data.csv", sep="|")

# 🔍 Search
query = st.text_input("Search mutual fund facts...")

# 💡 Example buttons
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

# 🤖 Answer logic
if query:
    result = df[df["question"].str.lower().str.contains(query.lower())]

    if not result.empty:
        answer = result.iloc[0]["answer"]
        source = result.iloc[0]["source"]

        st.markdown(f"""
        <div class="answer-box">
        <b style="color:#00D09C;">Answer</b><br><br>
        {answer}<br><br>
        🔗 <b>Source:</b> {source}
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("⚠️ I only answer factual mutual fund questions. No advice.")
