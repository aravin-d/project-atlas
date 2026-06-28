from app.models import Chunk, Page


def chunk_pages(
    pages: list[Page],
    chunk_size: int = 1000,
    overlap: int = 200,
) -> list[Chunk]:
    """
    Splits pages into overlapping chunks.
    """

    chunks: list[Chunk] = []

    chunk_index = 0

    for page in pages:
        start = 0

        while start < len(page.text):
            end = start + chunk_size

            chunks.append(
                Chunk(
                    page_number=page.page_number,
                    chunk_index=chunk_index,
                    text=page.text[start:end],
                )
            )

            chunk_index += 1
            start += chunk_size - overlap

    return chunks