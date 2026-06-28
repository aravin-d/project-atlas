from pathlib import Path

from app.chunking.chunker import chunk_pages
from app.loaders.pdf_loader import extract_pages


PDF_PATH = Path("data/documents/sample.pdf")


def main():
    if not PDF_PATH.exists():
        print(f"PDF not found: {PDF_PATH}")
        print("Place a PDF inside data/documents/")
        return

    pages = extract_pages(str(PDF_PATH))
    chunks = chunk_pages(pages)

    print(f"Pages : {len(pages)}")
    print(f"Chunks: {len(chunks)}")

    if chunks:
        print()
        print("First chunk")
        print("-" * 60)
        print(chunks[0])


if __name__ == "__main__":
    main()