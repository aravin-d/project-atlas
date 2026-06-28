from pathlib import Path

from pypdf import PdfReader

from app.models import Page


def extract_pages(pdf_path: str) -> list[Page]:
    """
    Reads a PDF and returns a list of Page objects.
    """

    reader = PdfReader(pdf_path)

    source = Path(pdf_path).name

    pages = []

    for page_number, page in enumerate(reader.pages, start=1):

        text = page.extract_text()

        if not text:
            continue

        pages.append(
            Page(
                page_number=page_number,
                text=text,
                source=source
            )
        )

    return pages