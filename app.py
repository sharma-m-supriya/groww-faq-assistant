import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- PAGE CONFIG ---------------- #
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
    margin-bottom: 20px;
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
    margin-left: auto;
    margin-right: auto;
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
    margin: 5px;
}

.stButton > button:hover {
    background: #00D09C;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO ---------------- #
st.markdown('<div class="center">', unsafe_allow_html=True)

st.markdown('<div class="title">Groww your knowledge 📈</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask factual mutual fund questions</div>', unsafe_allow_html=True)

# Info box
st.info("""
I can answer:
• Mutual fund basics (NAV, SIP, SWP)  
• Fund details (expense ratio, exit load)  
• Rules (lock-in, taxation)  
• Statements & downloads  

❌ I do NOT give investment advice
""")

# Search input
query = st.text_input(
    "",
    placeholder="Try: ELSS lock-in, NAV meaning, exit load SBI fund..."
)

# Suggested questions
st.write("### 💡 Try asking:")

examples = [
    "What is ELSS lock-in period?",
    "What is exit load in SBI Bluechip Fund?",
    "Minimum SIP amount for mutual funds?",
    "What is NAV in mutual funds?",
    "How to download capital gains statement?",
    "Who regulates mutual funds in India?"
]

cols = st.columns(2)

for i, q in enumerate(examples):
    with cols[i % 2]:
        if st.button(q):
            query = q

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

    # Reject advice queries
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
        st.warning("⚠️ Couldn't find exact answer. Try asking like:")
        st.write("- What is NAV?")
        st.write("- What is ELSS lock-in?")
        st.write("- Minimum SIP amount?")
