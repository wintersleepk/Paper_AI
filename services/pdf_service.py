import fitz
import math
import tempfile
import os
import hashlib

from models.paper import Paper


class PDFService:

    def load(self, uploaded_file):

        paper = Paper()

        paper.filename = uploaded_file.name

        pdf_bytes = uploaded_file.read()

        paper.pdf_hash = hashlib.sha256(
            pdf_bytes
        ).hexdigest()

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as tmp:

            tmp.write(pdf_bytes)

            pdf_path = tmp.name

        try:

            document = fitz.open(pdf_path)

            paper.pages = len(document)

            full_text = []

            pages_data = []

            word_count = 0

            for page_number, page in enumerate(
                document,
                start=1
            ):

                text = page.get_text("text")

                if not text:

                    continue

                full_text.append(text)

                pages_data.append(

                    {

                        "page": page_number,

                        "text": text,

                        "section": f"Page {page_number}"

                    }

                )

                paper.sections.append(

                    {

                        "page": page_number,

                        "section": f"Page {page_number}"

                    }

                )

                word_count += len(text.split())

            paper.full_text = "\n\n".join(full_text)

            paper.metadata["pages_data"] = pages_data

            paper.metadata["word_count"] = word_count

            paper.reading_time = max(

                1,

                math.ceil(word_count / 220)

            )

            metadata = document.metadata or {}

            paper.title = metadata.get(

                "title",

                ""

            ).strip()

            author_string = metadata.get(

                "author",

                ""

            ).strip()

            if author_string:

                paper.authors = [

                    author.strip()

                    for author in author_string.replace(

                        ";",

                        ","

                    ).split(",")

                    if author.strip()

                ]

            document.close()

        finally:

            if os.path.exists(pdf_path):

                os.remove(pdf_path)

        return paper