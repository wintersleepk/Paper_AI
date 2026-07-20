import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph
)

from reportlab.lib.styles import getSampleStyleSheet


class ExportService:

    def export(self, paper):

        os.makedirs(
            "exports",
            exist_ok=True
        )

        filename = os.path.join(
            "exports",
            paper.filename.replace(
                ".pdf",
                "_report.pdf"
            )
        )

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        content = str(
            paper.summary
        ).replace(
            "\n",
            "<br/>"
        )

        doc.build([
            Paragraph(
                "PaperMind AI Report",
                styles["Title"]
            ),
            Paragraph(
                content,
                styles["BodyText"]
            )
        ])

        return filename