from pdf_parser import extract_text
from pdf_ocr import run_ocr
from pdf_chunker import chunk_text
from pdf_embeddings import embed_chunks
from pdf_embeddings import embed_chunks
from pdf_retriever import retrieve
from pdf_summarizer import summarize


class PDFDirector:
    def process(self, pdf_path):
        text = extract_text(pdf_path)
        if len(text.strip()) < 100:
            text = run_ocr(pdf_path)

        chunks = chunk_text(text)
        embed_chunks(chunks)
        return {
            "text": text,
            "chunks": chunks
        }

    def answer_question(self, pdf_path, question):
        document = self.process(pdf_path)
        context = retrieve(question)
        return summarize(context, question)


def main():
    process()
    answer_questions()
    PDFDirector()


if __name__ == "__main":
    main()
