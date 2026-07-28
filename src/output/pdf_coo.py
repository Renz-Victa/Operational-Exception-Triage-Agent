from pdf_loader import load_pdf
from chunker import chunk_text
from embeddings import chunk_text
from vectordb import save_chunks

def process_pdf(file_path):
  text = load_pdf(file_path)
  chunks = chunk_text(text)
  vectors = create_embeddings(chunks)
  save_chunks(chunks, vectors)
  return {
    "status": "success",
    "chunks": len(chunks)
  }

def index_pdf(file_path):
  text = read(file_path)
  chunks = extract(text)
  vectors = create_embeddings(chunks)
  save_chunks(chunks, vectors)
  return {
    "status": "success",
    "chunks": len(chunks)
  }

def reindex_pdf(index_pdf):
  delete = delete(embeddings)
  read = read(index_pdf)
  text = load_pdf(index_pdf)
  chunks = chunk_text(text)
  vectors = create_embeddings(chunks)
  save_chunks(chunks, vectors)
  return {
    "status": "success",
    "chunks": len(chunks)
  }

def delete_pdf(file_path):
  file = delete(file_path)
  text = delete(chunks)
  embeddings = delete(embeddings)
  metadata = delete(metadata)
  remove = delete(vector_db)

def get_pdf_status(file_path):
  status = get_pdf_status(file_path)
  return {
    "status": "success",
    "progress": 100
  }

def main():
  process_pdf()
  index_pdf()
  reindex_pdf()
  delete_pdf()
  get_pdf_status()

if __name__ == "__main__":
  main()