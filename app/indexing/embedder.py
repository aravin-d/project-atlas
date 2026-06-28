import ollama

from app.models import Chunk, EmbeddedChunk


EMBEDDING_MODEL = "nomic-embed-text"


def embed_chunks(chunks: list[Chunk]) -> list[EmbeddedChunk]:

    embedded_chunks = []

    total = len(chunks)

    for index, chunk in enumerate(chunks, start=1):

        response = ollama.embed(
            model=EMBEDDING_MODEL,
            input=chunk.text
        )

        embedding = response["embeddings"][0]

        embedded_chunks.append(
            EmbeddedChunk(
                chunk=chunk,
                embedding=embedding
            )
        )

        if index % 25 == 0 or index == total:
            print(f"Embedded {index}/{total}")

    return embedded_chunks