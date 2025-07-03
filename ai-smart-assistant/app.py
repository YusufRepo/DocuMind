import streamlit as st
from modules.parser import extract_text_from_upload
from modules.vector_store import create_index, query_index
from modules.llm_interface import ask_llm

st.image("https://www.amital.co.id/favicon.ico", width=200)

st.title("DocuMind by Aku Mitra Digital")

uploaded_file = st.file_uploader("Upload file (PDF/TXT)", type=["pdf", "txt"])

if uploaded_file:
    with st.spinner("Processing file..."):
        text = extract_text_from_upload(uploaded_file)
        index = create_index(text)
        st.success("File indexed successfully!")

        question = st.text_input("Ask something...")
        if question:
            with st.spinner("Searching and answering..."):
                results = query_index(question, index, k=3)
                context = "\n\n".join(results)
                answer = ask_llm(question, context)
                st.markdown("### Answer:")
                st.write(answer)