# utils.py

import os
from PyPDF2 import PdfReader

def load_text(file_path: str) -> str:
    """Load text from a .txt file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()
    except Exception as e:
        return f"Error reading file: {e}"

def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF file."""
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text.strip()
    except Exception as e:
        return f"Error reading PDF: {e}"

def clean_text(text: str) -> str:
    """Remove extra whitespace and line breaks."""
    return " ".join(text.split())


# file_path = r"C:\Users\lapto\Downloads\8a4c843fd7684f55860e5c105e7f8453.pdf"
# resume_text = clean_text(extract_text_from_pdf(file_path))
# print(resume_text)