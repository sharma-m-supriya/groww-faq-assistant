import streamlit as st
import pandas as pd

st.set_page_config(page_title="Groww FAQ Assistant")

st.title("📊 Groww FAQ Assistant")
st.write("Ask me factual questions about SBI Mutual Funds.")

# Load dataset
df = pd.read_csv("data.csv")

# Example questions
st.markdown("### Example Questions:")
st.write("- Expense ratio of SBI Bluechip Fund?")
st.write("- ELSS lock-in period?")
st.write("- How to download capital gains statement?")

# Input
user_query = st.text_input("Enter your question:")

def find_answer(query):
    query = query.lower()
    
    for index, row in df.iterrows():
        if row["question"].lower() in query:
            return f"{row['answer']} (Source: {row['source']})"
    
    return None

def is_advice_query(query):
    advice_keywords = ["should i", "which is better", "recommend", "invest"]
    return any(word in query.lower() for word in advice_keywords)

if st.button("Analyze"):
    if user_query:
        
        # Check for advice
        if is_advice_query(user_query):
            st.error("I can only provide factual information and cannot give investment advice.")
        
        else:
            answer = find_answer(user_query)
            
            if answer:
                st.success(answer + " Last updated: April 2026.")
            else:
                st.warning("No exact match found. Please ask a factual question.")
    
    else:
        st.warning("Please enter a question")

# Footer
st.markdown("---")
st.caption("Facts only. No investment advice.")
