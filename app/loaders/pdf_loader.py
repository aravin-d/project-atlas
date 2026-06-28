from pypdf import PdfReader

from app.models import Page


def extract_pages(pdf_path: str) -> list[Page]:
    """
    Reads a PDF and converts each page into a Page object.
    """

    reader = PdfReader(pdf_path)

    pages: list[Page] = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if not text:
            continue

        pages.append(
            Page(
                page_number=page_number,
                text=text,
            )
        )

    return pages