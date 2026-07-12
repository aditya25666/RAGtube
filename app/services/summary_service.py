import json

from google.genai import types

from app.config.constants import LLM_MODEL
from app.config.genai import client
from app.prompts.summary_prompt import SUMMARY_PROMPT
from app.schemas.summary_schema import SUMMARY_SCHEMA
from app.services.transcript_storage_service import (
    TranscriptStorageService,
)


class SummaryService:
    """
    Generates a structured summary of a YouTube video.
    """

    def __init__(self):

        self.storage = TranscriptStorageService()

    def generate_summary(
        self,
        video_id: str,
    ):

        transcript = self.storage.load(video_id)

        prompt = SUMMARY_PROMPT.format(
            transcript=transcript
        )

        response = client.models.generate_content(
            model=LLM_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=SUMMARY_SCHEMA,
                temperature=0.2,
            ),
        )

        summary = json.loads(response.text)

        return {
            "video_id": video_id,
            "summary": summary,
        }