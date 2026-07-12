from langchain_core.documents import Document


class DocumentService:
    """
    Converts transcript blocks into LangChain Document objects.
    """

    @staticmethod
    def create_documents(video_id: str, blocks: list) -> list[Document]:
        """
        Convert transcript blocks into LangChain Documents.

        Args:
            video_id: YouTube video ID
            blocks: Output from BlockService

        Returns:
            List of LangChain Document objects.
        """

        documents = []

        for index, block in enumerate(blocks):

            document = Document(
                page_content=block["text"],
                metadata={
                    "video_id": video_id,
                    "chunk_id": index,
                    "start": block["start"],
                    "end": block["end"],
                    "source": "youtube",
                },
            )

            documents.append(document)

        return documents