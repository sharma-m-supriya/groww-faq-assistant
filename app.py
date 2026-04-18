import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Groww FAQ Assistant", layout="centered")

# Groww-style CSS
st.markdown("""
<style>
body {
    background-color: #F7F9FB;
}
.title {
    text-align: center;
    font-size: 52px;
    font-weight: 700;
    color: #2E2E2E;
}
.subtitle {
    text-align: center;
    color: #6b7280;
    font-size: 18px;
}
.green-btn {
    background-color: #00D09C;
    color: white;
    border-radius: 25px;
    padding: 10px 25px;
    text-align: center;
    display: inline-block;
    font-weight: 600;
}
.answer-box {
    background-color: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.06);
    margin-top: 20px;
}
.header {
    display: flex;
    justify-content: space-between;
    font-weight: 600;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# Navbar
col1, col2 = st.columns([3,1])
with col1:
    st.markdown("### Groww FAQ Assistant")
with col2:
    st.markdown("<p style='text-align:right;color:#00D09C;'>Facts only</p>", unsafe_allow_html=True)

# Hero Section
st.markdown('<p class="title">Groww your knowledge 📈</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Ask factual mutual fund questions</p>', unsafe_allow_html=True)

st.write("")

# Load CSV
df = pd.read_csv("data.csv", sep="|")

# Input
query = st.text_input("🔍 Ask your question")

# Example buttons
st.write("### Try these:")
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
        <b style="color:#00D09C;">Answer</b><br><br>
        {answer}<br><br>
        🔗 <span style="color:#00D09C;">Source:</span> {source}
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("⚠️ I only answer factual mutual fund questions. No advice.")
