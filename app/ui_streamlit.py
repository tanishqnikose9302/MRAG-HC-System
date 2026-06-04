import streamlit as st
from rag.pipeline import rag_pipeline

st.title("MRAG-HC AI System")

query = st.text_input("Ask your question")

if st.button("Search"):
    answer, docs = rag_pipeline(query, st.session_state.vectorstore)

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Sources")
    st.write(docs)
