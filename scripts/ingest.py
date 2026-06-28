from app.loaders.pdf_loader import extract_pages
from app.chunking.chunker import chunk_pages

pages = extract_pages("docs/lms.pdf")

chunks = chunk_pages(pages)

print(f"Pages: {len(pages)}")
print(f"Chunks: {len(chunks)}")

print(chunks[0])