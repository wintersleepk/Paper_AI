class SectionService:

    def detect_sections(self, paper):

        sections = []

        for page in paper.metadata.get("pages_data", []):

            sections.append(

                {

                    "title": page.get(

                        "section",

                        "Unknown"

                    ),

                    "page": page.get(

                        "page",

                        0

                    )

                }

            )

        paper.sections = sections

        return paper