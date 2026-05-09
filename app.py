import streamlit as st
from src.semantic_search import semantic_search

st.set_page_config(
    page_title="AI Co-op Career Intelligence Assistant",
    layout="wide"
)

st.title("AI Co-op Career Intelligence Assistant")

st.write(
    "Semantic search across co-op reports, company advice, interview tips, and student experiences."
)

query = st.text_input("Enter your search query:")
top_k = st.slider("Number of results", 1, 10, 5)

if query:
    results = semantic_search(query, top_k=top_k)

    st.subheader("Top Semantic Results")

    if not results:
        st.warning("No results found.")
    else:
        for result in results:
            st.markdown("---")
            st.write(f"**File:** {result['file_name']}")
            st.write(f"**Distance:** {result['score']}")
            st.write(f"**Path:** `{result['path']}`")
            st.write(result["text"][:1000])