from google.genai import types

from app.config.constants import EMBEDDING_MODEL
from app.config.genai import client


class EmbeddingService:
    """
    Handles embedding generation using Google's official GenAI SDK.
    """

    @staticmethod
    def embed_documents(texts: list[str]) -> list[list[float]]:
        """
        Generate embeddings for multiple texts.
        """

        response = client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=texts,
            config=types.EmbedContentConfig(
                task_type="RETRIEVAL_DOCUMENT"
            ),
        )

        return [
            embedding.values
            for embedding in response.embeddings
        ]

    @staticmethod
    def embed_query(query: str) -> list[float]:
        """
        Generate embedding for a user query.
        """

        response = client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=query,
            config=types.EmbedContentConfig(
                task_type="RETRIEVAL_QUERY"
            ),
        )

        return response.embeddings[0].values