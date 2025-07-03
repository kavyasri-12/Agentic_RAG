# main.py

import streamlit as st
from coordinator import Coordinator

st.set_page_config(page_title="Agentic RAG Chatbot", layout="wide")

st.title("Agentic RAG Chatbot with MCP")

openai_api_key = st.text_input("Enter Your Groq Key", type="password")

uploaded_files = st.file_uploader("Upload your documents (PDF, PPTX, DOCX, CSV, TXT)", accept_multiple_files=True)

query = st.text_input("Ask a question based on your documents")

if st.button("Ask") and uploaded_files and query and openai_api_key:
    coordinator = Coordinator(openai_api_key)
    with st.spinner("Processing..."):
        answer, sources = coordinator.handle(uploaded_files, query)
        st.markdown("### Answer:")
        st.write(answer)
        st.markdown("---")
        st.markdown("### Source Context:")
        for i, s in enumerate(sources):
            st.markdown(f"**Chunk {i+1}:** {s[:500]}...")

