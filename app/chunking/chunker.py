from app.models import Page, Chunk


def chunk_pages(
    pages: list[Page],
    chunk_size: int = 1000,
    overlap: int = 200
) -> list[Chunk]:

    chunks = []

    chunk_id = 1

    for page in pages:

        start = 0

        while start < len(page.text):

            end = start + chunk_size

            chunk_text = page.text[start:end]

            chunks.append(
                Chunk(
                    chunk_id=chunk_id,
                    text=chunk_text,
                    page=page.page_number,
                    source=page.source
                )
            )

            chunk_id += 1

            start += chunk_size - overlap

    return chunks