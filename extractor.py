import os
from pdfminer.high_level import extract_text
from docx import Document as DocxDocument

def extract_pdf(path):
    raw = extract_text(path)
    # Simple split by headings (e.g., lines in ALL CAPS)
    lines = raw.splitlines()
    sections = []
    current = {"heading": "Introduction", "content": []}
    for line in lines:
        if line.isupper() and len(line.split()) < 8:
            sections.append(current)
            current = {"heading": line.strip(), "content": []}
        else:
            current["content"].append(line)
    sections.append(current)
    return [(s["heading"], "\n".join(s["content"])) for s in sections if s["content"]]

def extract_docx(path):
    doc = DocxDocument(path)
    sections = []
    current = {"heading": "Introduction", "content": []}
    for p in doc.paragraphs:
        text = p.text.strip()
        if p.style.name.startswith('Heading'):
            sections.append(current)
            current = {"heading": text, "content": []}
        else:
            current["content"].append(text)
    sections.append(current)
    return [(s["heading"], "\n".join(s["content"])) for s in sections if s["content"]]

def extract_text_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    # treat entire file as one section
    return [("Full Document", text)]
