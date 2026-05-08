from pathlib import Path
from pypdf import PdfReader
from docx import Document as DocReader
import json

RAW_DATA = Path("data/raw")
OUTPUT_DATA = Path("data/processed")

Documents = []

# Creating 
def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
        else:
            print(f"Error reading pdf in {file_path}")
    return text

def extract_text_from_docx(file_path):
    reader = DocReader(file_path)
    text = ""
    for paragraph in reader.paragraphs:
        extracted = paragraph.text
        if extracted:
            text += extracted + "\n"
        else:
            print(f"Error reading docx in {file_path}")
    return text

for file in RAW_DATA.rglob("*.*"):
    if file.suffix.lower() == ".pdf":
        text = extract_text_from_pdf(file)
    elif file.suffix.lower() == ".docx":
        text = extract_text_from_docx(file)
    else:
        print(f"Unsupported file type: {file}")
        continue
    
    document = {
        "file_name": file.name,
        "path": str(file),
        "text": text
    }
    Documents.append(document)

# Save the extracted text to a JSON file
with open(OUTPUT_DATA / "documents.jsonl", "w") as file:
    for doc in Documents:
        json.dump(doc, file)
        file.write("\n")
