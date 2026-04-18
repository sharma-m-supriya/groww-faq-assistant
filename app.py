import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Page config
st.set_page_config(layout="wide")

# ---------------- UI ---------------- #

st.markdown("""
<style>
body {
    background-color: #F7F9FB;
}

.block-container {
    padding-top: 2rem;
}

/* Center content */
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
}

/* Answer box */
.answer {
    background: #FFFFFF;
    padding: 25px;
    border-radius: 20px;
    margin-top: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.06);
    max-width: 800px;
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
}

.stButton > button:hover {
    background: #00D09C;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Hero section
st.markdown('<div class="center">', unsafe_allow_html=True)
st.markdown('<div class="title">Groww your wealth</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask factual mutual fund questions</div>', unsafe_allow_html=True)

query = st.text_input("", placeholder="Search mutual fund facts...")

# Example buttons
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

# ---------------- DATA ---------------- #

df = pd.read_csv("data.csv", sep="|")

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

questions = df["question"].tolist()
question_embeddings = model.encode(questions)

# ---------------- SMART SEARCH ---------------- #

def get_best_answer(user_query):
    query_embedding = model.encode([user_query])
    scores = cosine_similarity(query_embedding, question_embeddings)[0]
    
    best_index = scores.argmax()
    best_score = scores[best_index]
    
    if best_score < 0.4:
        return None
    
    return df.iloc[best_index]

# ---------------- RESPONSE ---------------- #

if query:

    # ❌ Reject advice questions
    if any(word in query.lower() for word in ["buy", "invest", "best", "should"]):
        st.warning("⚠️ I only provide factual information. No investment advice.")
        st.stop()

    st.write(f"💬 You asked: *{query}*")

    result = get_best_answer(query)

    if result is not None:
        answer = result["answer"]
        source = result["source"]

        st.markdown(f"""
        <div class="answer">
            <div class="green">Answer</div><br>
            {answer}<br><br>
            🔗 <a href="{source}" target="_blank">View Source</a>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("⚠️ Sorry, I couldn't find a factual answer.")
