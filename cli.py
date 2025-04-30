import argparse, os
from database import init_db, SessionLocal
from models import Document, Section
from extractor import extract_pdf, extract_docx, extract_text_file
from summarizer import summarize_text

def ingest_file(db, path):
    ext = os.path.splitext(path)[1].lower()
    if ext == '.pdf':
        data = extract_pdf(path)
    elif ext in ('.docx',):
        data = extract_docx(path)
    else:
        data = extract_text_file(path)

    doc = Document(filename=os.path.basename(path))
    db.add(doc); db.commit()
    for heading, content in data:
        summary = summarize_text(content)
        sec = Section(document_id=doc.id, heading=heading, content=content, summary=summary)
        db.add(sec)
    db.commit()
    print(f"Ingested and summarized {len(data)} sections from {path}")

def list_docs(db):
    for doc in db.query(Document).all():
        print(f"{doc.id}: {doc.filename}")

def view_summaries(db, doc_id):
    secs = db.query(Section).filter_by(document_id=doc_id).all()
    for s in secs:
        print(f"## {s.heading}\n{s.summary}\n")

def main():
    init_db()
    db = SessionLocal()
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd")
    p1 = sub.add_parser("ingest"); p1.add_argument("path")
    p2 = sub.add_parser("list")
    p3 = sub.add_parser("summaries"); p3.add_argument("doc_id", type=int)
    args = parser.parse_args()
    if args.cmd == "ingest":
        ingest_file(db, args.path)
    elif args.cmd == "list":
        list_docs(db)
    elif args.cmd == "summaries":
        view_summaries(db, args.doc_id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
