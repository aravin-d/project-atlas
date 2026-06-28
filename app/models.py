from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Document:
    filename: str
    file_hash: str
    imported_at: datetime


@dataclass(slots=True)
class Page:
    page_number: int
    text: str


@dataclass(slots=True)
class Chunk:
    page_number: int
    chunk_index: int
    text: str


@dataclass(slots=True)
class EmbeddedChunk:
    chunk: Chunk
    embedding: list[float]