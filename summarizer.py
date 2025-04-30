from transformers import pipeline

# Load once at startup
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    # Chunk if too long
    max_chunk = 1000
    sentences = text.split('. ')
    chunks = []
    current = ""
    for sent in sentences:
        if len(current) + len(sent) < max_chunk:
            current += sent + '. '
        else:
            chunks.append(current)
            current = sent + '. '
    chunks.append(current)
    # Summarize each and join
    summaries = [summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
                 for chunk in chunks]
    return " ".join(summaries)
