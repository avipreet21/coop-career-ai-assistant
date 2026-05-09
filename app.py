import streamlit as st
from src.rag_answers import generate_answer

st.set_page_config(
    page_title="AI Co-op Career Intelligence Assistant",
    layout="wide"
)

st.title("AI Co-op Career Intelligence Assistant")

st.write(
    "Ask questions about co-op reports, company advice, interview tips, and student experiences."
)

question = st.text_input("Ask a question:")
top_k = st.slider("Number of sources to use", 1, 10, 5)

if question:
    with st.spinner("Searching documents and generating answer..."):
        answer, sources = generate_answer(question, top_k=top_k)

    st.subheader("AI Answer")
    st.write(answer)

    st.subheader("Sources")

    for source in sources:
        st.markdown("---")
        st.write(f"**File:** {source['file_name']}")
        st.write(f"**Distance:** {source['score']}")
        st.write(f"**Path:** `{source['path']}`")
        st.write(source["text"][:800])