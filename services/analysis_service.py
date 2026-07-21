from services.gemini_service import GeminiService


class AnalysisService:

    def __init__(self):
        self.client = GeminiService()

    def generate_all(self, paper):

        prompt = f"""
You are an expert research paper analyst.

Create a clean markdown report.

Include:

# Executive Summary

# Study Notes

# Research Insights

# Knowledge Check

Generate 10 MCQs.

Each MCQ must have:

A.
B.
C.
D.

Return ONLY markdown.

Paper:

{paper.full_text[:15000]}
"""

        response = self.client.generate(prompt)

        if not response:
            response = """
# Executive Summary

Analysis could not be generated.

# Study Notes

No study notes available.

# Research Insights

No insights available.

# Knowledge Check

No quiz available.
"""

        paper.summary = response

        return paper
