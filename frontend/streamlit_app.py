# frontend/streamlit_app.py

import os
import requests
import streamlit as st

# Read the API URL (defaults to localhost)
API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(
    page_title="HealthMLOpsX Chat",
    page_icon="🤖",
    layout="centered"
)

st.title("HealthMLOpsX Chat")
st.markdown("Ask your health-related questions and get RAG-powered answers!")

# Initialize chat history in session state
if "history" not in st.session_state:
    st.session_state.history = []

def send_query(query: str):
    try:
        resp = requests.get(f"{API_URL}/ask", params={"query": query}, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data["answer"], data["sources"]
    except Exception as e:
        return f"❌ Error: {e}", []

# Input box (no session_state key, so we just read it once)
query = st.text_input("Your question:")

# When the user clicks Send, capture the current query, add to history
if st.button("Send") and query:
    answer, sources = send_query(query)
    st.session_state.history.append((query, answer, sources))
    # NO manual clearing of session_state.input here

# Display history in reverse (newest first)
for q, a, srcs in reversed(st.session_state.history):
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Bot:** {a}")
    if srcs:
        with st.expander("Sources"):
            for s in srcs:
                st.write(f"- {s['text']} (score: {s['score']:.3f})")
    st.markdown("---")
