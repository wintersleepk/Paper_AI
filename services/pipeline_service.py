from services.pdf_service import PDFService
from services.vector_service import VectorService
from services.analysis_service import AnalysisService


class PipelineService:

    def __init__(self):

        self.pdf = PDFService()

        self.vector = VectorService()

        self.analysis = AnalysisService()

    def process(self, uploaded_file):

        paper = self.pdf.load(uploaded_file)

        cached = self.vector.load(paper)

        if cached:

            return cached

        paper = self.vector.build(paper)

        try:

            paper = self.analysis.generate_all(paper)

        except Exception as e:

            print(f"Analysis Error: {e}")

            paper.summary = "Analysis could not be generated."

            paper.study_notes = ""

            paper.insights = ""

            paper.quiz = []

        self.vector.save(paper)

        return paper

    def rebuild_analysis(self, paper):

        try:

            paper = self.analysis.generate_all(paper)

            self.vector.save(paper)

        except Exception as e:

            print(f"Analysis Error: {e}")

        return paper

    def rebuild_embeddings(self, paper):

        paper = self.vector.build(paper)

        self.vector.save(paper)

        return paper