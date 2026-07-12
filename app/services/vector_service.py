import uuid

from langchain_core.documents import Document
from langchain_qdrant import QdrantVectorStore

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    FieldCondition,
    Filter,
    FilterSelector,
    MatchValue,
    VectorParams,
)

from app.config.constants import (
    COLLECTION_NAME,
    TOP_K,
)

from app.services.gemini_embeddings import GeminiEmbeddings


class VectorService:

    def __init__(self):

        self.client = QdrantClient(
            path="data/qdrant",
        )

        self.embeddings = GeminiEmbeddings()

        self._create_collection()

        self.vector_store = QdrantVectorStore(
            client=self.client,
            collection_name=COLLECTION_NAME,
            embedding=self.embeddings,
        )

    def _create_collection(self):

        collections = self.client.get_collections().collections

        names = [
            collection.name
            for collection in collections
        ]

        if COLLECTION_NAME in names:
            return

        sample = self.embeddings.embed_query(
            "hello"
        )

        self.client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=len(sample),
                distance=Distance.COSINE,
            ),
        )

    def add_documents(
        self,
        documents,
    ):

        ids = []

        for index, document in enumerate(documents):

            video_id = document.metadata["video_id"]

            ids.append(
                str(
                    uuid.uuid5(
                        uuid.NAMESPACE_URL,
                        f"{video_id}_{index}",
                    )
                )
            )

        self.vector_store.add_documents(
            documents=documents,
            ids=ids,
        )

    def search(
        self,
        video_id: str,
        query: str,
        k: int = TOP_K,
    ) -> list[Document]:

        query_vector = self.embeddings.embed_query(
            query
        )

        results = self.client.query_points(
            collection_name=COLLECTION_NAME,
            query=query_vector,
            limit=k,
            query_filter=Filter(
                must=[
                    FieldCondition(
                        key="metadata.video_id",
                        match=MatchValue(
                            value=video_id,
                        ),
                    )
                ]
            ),
            with_payload=True,
        ).points

        documents = []

        for point in results:

            payload = point.payload

            metadata = payload["metadata"]

            documents.append(
                Document(
                    page_content=payload["page_content"],
                    metadata=metadata,
                )
            )

        return documents

    def delete_video(
        self,
        video_id: str,
    ):

        self.client.delete(
            collection_name=COLLECTION_NAME,
            points_selector=FilterSelector(
                filter=Filter(
                    must=[
                        FieldCondition(
                            key="metadata.video_id",
                            match=MatchValue(
                                value=video_id,
                            ),
                        )
                    ]
                )
            ),
        )