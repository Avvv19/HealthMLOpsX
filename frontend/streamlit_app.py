import streamlit as st
import requests

st.title("HealthMLOpsX RAG Chatbot")

query = st.text_input("Ask a health-related question:")

if st.button("Submit") and query:
    resp = requests.get("http://localhost:8000/ask", params={"query": query})
    st.json(resp.json())
