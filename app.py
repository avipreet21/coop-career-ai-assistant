from pathlib import Path
from src.search import load_documents
import streamlit as st


st.set_page_config(page_title="Ai Co op Career intelligence assistance", layout="wide")

st.title("Ai Co op Career intelligence assistance")

st.write(
    "Search co-op reports, company advice, interview tips, and student experiences."
)

document = load_documents(Data_file=Path("data/processed/documents.jsonl"))

query = st.text_input("Enter your search query:")

if query:
    results = search_documents(query, document)

    st.subheader("Top Results")

    if not results:
        st.warning("No results found.")
    else:
        for result in results[:5]:
            doc = result["document"]

            st.markdown("---")
            st.write(f"**File:** {doc['file_name']}")
            st.write(f"**Score:** {result['score']}")
            st.write(f"**Path:** `{doc['path']}`")
            st.write(doc["text"][:500])
            
