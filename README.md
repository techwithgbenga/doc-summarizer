# Intelligent Document Processing & Summarization Pipeline

## Overview
A Python tool to ingest PDFs, DOCX, and TXT files; extract and structure text; summarize each section with a transformer model; and expose results via CLI or REST API.

## Features
- **Ingestion**: PDF, Word, and plain-text support  
- **Extraction**: Section splitting by headings  
- **Summarization**: Hugging Face BART summarizer  
- **Storage**: SQLite + SQLAlchemy  
- **Interfaces**: CLI & Flask API  

## Setup
```bash
git clone https://github.com/techwithgbenga/doc_summarizer.git
cd doc_summarizer
pip install -r requirements.txt
```
## Usage
### CLI
```bash
python cli.py ingest /path/to/file.pdf
python cli.py list
python cli.py summaries 1
```
### API
```bash
python api.py
# POST /upload with form-file “file”
# GET /documents
# GET /summaries/<doc_id>
```
## Future Enhancements
- Add OAuth2 for API auth
- Support HTML and Markdown inputs
- Integrate with a frontend UI (React/Vue)
- Customizable models (e.g., T5, GPT-style APIs)

