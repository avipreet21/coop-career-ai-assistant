import streamlit as st
from src.search import search_documents

st.set_page_config(page_title="Ai Co op Career intelligence assistance", layout="wide")

st.title("Ai Co op Career intelligence assistance")

st.write(
    "Search co-op reports, company advice, interview tips, and student experiences."
)

document = load_documents()

query = st.text_input("Enter your search query:")

if query:
    results = search_documents(query, documents, top_k=5)

    st.subheader("Top Results")

    if not results:
        st.warning("No results found.")
    else:
        for result in results:
            st.markdown("---")
            st.write(f"**File:** {result['file_name']}")
            st.write(f"**Score:** {result['score']}")
            st.write(f"**Path:** `{result['path']}`")
            st.write(result["preview"])
