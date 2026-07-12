import json

from google.genai import types

from app.config.constants import LLM_MODEL
from app.config.genai import client


class GenerationService:
    """
    Handles all interactions with Gemini.
    """

    @staticmethod
    def generate(
        prompt: str,
        response_schema=None,
        temperature: float = 0.2,
    ):
        """
        Generate a response from Gemini.

        NOTE:
        Structured output is temporarily disabled for debugging.
        """

        print("=" * 100)
        print("PROMPT SENT TO GEMINI")
        print("=" * 100)
        print(prompt)
        print("=" * 100)

        response = client.models.generate_content(
            model=LLM_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=temperature,
            ),
        )

        print("=" * 100)
        print("RAW GEMINI RESPONSE")
        print("=" * 100)
        print(response.text)
        print("=" * 100)

        return {
            "answer": response.text,
            "confidence": "Debug",
        }