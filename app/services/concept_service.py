import json

from google.genai import types

from app.config.constants import LLM_MODEL
from app.config.genai import client
from app.prompts.concept_prompt import CONCEPT_PROMPT
from app.schemas.concept_schema import CONCEPT_SCHEMA
from app.services.transcript_storage_service import (
    TranscriptStorageService,
)


class ConceptService:
    """
    Generates important concepts from a YouTube transcript.
    """

    def __init__(self):

        self.storage = TranscriptStorageService()

    def generate_concepts(
        self,
        video_id: str,
    ):

        transcript = self.storage.load(video_id)

        prompt = CONCEPT_PROMPT.format(
            transcript=transcript
        )

        response = client.models.generate_content(
            model=LLM_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=CONCEPT_SCHEMA,
                temperature=0.2,
            ),
        )

        concepts = json.loads(response.text)

        return {
            "video_id": video_id,
            "concepts": concepts,
        }