from flask import Flask, request, jsonify
from database import init_db, SessionLocal
from models import Document, Section
from cli import ingest_file
import os

app = Flask(__name__)
init_db()

@app.route("/upload", methods=["POST"])
def upload():
    f = request.files["file"]
    save_path = os.path.join("uploads", f.filename)
    os.makedirs("uploads", exist_ok=True)
    f.save(save_path)
    db = SessionLocal()
    ingest_file(db, save_path)
    return jsonify({"status": "ingested", "filename": f.filename})

@app.route("/documents", methods=["GET"])
def documents():
    db = SessionLocal()
    docs = db.query(Document).all()
    return jsonify([{"id": d.id, "filename": d.filename} for d in docs])

@app.route("/summaries/<int:doc_id>", methods=["GET"])
def summaries(doc_id):
    db = SessionLocal()
    secs = db.query(Section).filter_by(document_id=doc_id).all()
    return jsonify([{"heading": s.heading, "summary": s.summary} for s in secs])

if __name__ == "__main__":
    app.run(debug=True)
