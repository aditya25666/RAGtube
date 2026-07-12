from typing import List

from google.genai import types
from langchain_core.embeddings import Embeddings

from app.config.constants import EMBEDDING_MODEL
from app.config.genai import client


class GeminiEmbeddings(Embeddings):
    """
    LangChain adapter around the official Google GenAI SDK.
    """

    def embed_documents(
        self,
        texts: List[str],
    ) -> List[List[float]]:

        response = client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=texts,
            config=types.EmbedContentConfig(
                task_type="RETRIEVAL_DOCUMENT",
            ),
        )

        return [
            embedding.values
            for embedding in response.embeddings
        ]

    def embed_query(
        self,
        text: str,
    ) -> List[float]:

        response = client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=text,
            config=types.EmbedContentConfig(
                task_type="RETRIEVAL_QUERY",
            ),
        )

        return response.embeddings[0].values