import google.generativeai as genai

from config import (
    GEMINI_API_KEY,
    GEMINI_MODEL
)


class GeminiService:

    def __init__(self):

        genai.configure(
            api_key=GEMINI_API_KEY
        )

        self.model = genai.GenerativeModel(
            GEMINI_MODEL
        )

    def generate(self, prompt):

        try:

            response = self.model.generate_content(
                prompt
            )

            text = getattr(
                response,
                "text",
                ""
            )

            if not text:

                return ""

            return text

        except Exception as e:

            print(
                f"Gemini Error: {e}"
            )

            return ""