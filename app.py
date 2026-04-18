import streamlit as st

st.set_page_config(page_title="Groww FAQ Assistant")

st.title("📊 Groww FAQ Assistant")

st.write("Ask me factual questions about SBI Mutual Funds.")

# Example questions
st.markdown("### Example Questions:")
st.write("- Expense ratio of SBI Bluechip Fund?")
st.write("- ELSS lock-in period?")
st.write("- How to download capital gains statement?")

# Input
user_query = st.text_input("Enter your question:")

if st.button("Analyze"):
    if user_query:
        st.success("Answer will appear here (next step)")
    else:
        st.warning("Please enter a question")

# Footer
st.markdown("---")
st.caption("Facts only. No investment advice.")
