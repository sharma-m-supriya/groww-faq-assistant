import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# 🔥 CLEAN MODERN CSS
st.markdown("""
<style>

/* Remove ugly padding */
.block-container {
    padding-top: 2rem;
}

/* Background */
body {
    background-color: #F7F9FB;
}

/* Center everything */
.center {
    text-align: center;
}

/* Title */
.title {
    font-size: 64px;
    font-weight: 800;
    color: #2E2E2E;
}

/* Subtitle */
.subtitle {
    font-size: 18px;
    color: #6B7280;
    margin-bottom: 30px;
}

/* Search bar */
.stTextInput > div > div > input {
    border-radius: 40px;
    padding: 18px;
    font-size: 16px;
    border: 1px solid #ddd;
}

/* Answer bubble */
.answer {
    background: white;
    padding: 25px;
    border-radius: 20px;
    margin-top: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.06);
}

/* Green highlight */
.green {
    color: #00D09C;
    font-weight: 600;
}

/* Buttons */
.stButton > button {
    border-radius: 30px;
    border: 1px solid #00D09C;
    color: #00D09C;
    padding: 10px 20px;
}

.stButton > button:hover {
    background: #00D09C;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# 🧠 HERO SECTION
st.markdown('<div class="center">', unsafe_allow_html=True)

st.markdown('<div class="title">Groww your wealth</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask factual mutual fund questions</div>', unsafe_allow_html=True)

# 🔍 SEARCH BAR
query = st.text_input("", placeholder="Search mutual fund facts...")

# 💡 QUICK QUESTIONS
st.write("")
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

st.markdown('</div>', unsafe_allow_html=True)

# 📂 DATA
df = pd.read_csv("data.csv", sep="|")

# 🤖 RESPONSE
if query:
    result = df[df["question"].str.lower().str.contains(query.lower())]

    if not result.empty:
        answer = result.iloc[0]["answer"]
        source = result.iloc[0]["source"]

        st.markdown(f"""
        <div class="answer">
            <div class="green">Answer</div><br>
            {answer}<br><br>
            🔗 <span class="green">Source:</span> {source}
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("⚠️ Facts only. No investment advice.")
