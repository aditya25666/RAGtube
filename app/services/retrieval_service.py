from langchain_core.documents import Document

from app.services.vector_service import VectorService


class RetrievalService:

    def __init__(self):

        self.vector_service = VectorService()

    def retrieve(
        self,
        video_id: str,
        question: str,
    ) -> list[Document]:

        documents = self.vector_service.search(
            video_id=video_id,
            query=question,
        )

        documents.sort(
            key=lambda d: d.metadata.get(
                "start",
                0,
            )
        )
        
        print("=" * 80)
        print(f"Retrieved {len(documents)} documents")

        for doc in documents:
            print(doc.metadata)
            print(doc.page_content[:200])

        print("=" * 80)

        return documents