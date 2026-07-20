from services.gemini_service import GeminiService


class RAGService:

    def __init__(self):

        self.llm = GeminiService()

    def ask(self, paper, question):

        context = paper.full_text[:30000]

        history = self.build_history(

            paper.chat_history

        )

        prompt = f"""
You are PaperMind AI.

Answer ONLY using the provided research paper.

If the answer is not present,
say that it is not available in the paper.

Conversation History:

{history}

Research Paper:

{context}

User Question:

{question}

Rules:

1. Be technically accurate.

2. Use markdown.

3. Keep explanations concise.

4. Never make up information.

Answer:
"""

        try:

            answer = self.llm.generate(

                prompt

            )

        except Exception as e:

            answer = f"Error while generating answer:\n\n{e}"

        paper.chat_history.append(

            {

                "question": question,

                "answer": answer

            }

        )

        return answer

    def build_history(

        self,

        history,

        limit=4

    ):

        if not history:

            return "No previous conversation."

        text = []

        for item in history[-limit:]:

            text.append(

                f"""
User:

{item['question']}

Assistant:

{item['answer']}
"""

            )

        return "\n\n".join(text)