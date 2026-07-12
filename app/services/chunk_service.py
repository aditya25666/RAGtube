from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


class ChunkService:
    """
    Splits LangChain Documents into smaller overlapping chunks.
    """

    def __init__(
        self,
        chunk_size: int = 800,
        chunk_overlap: int = 150,
    ):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                "? ",
                "! ",
                " ",
                "",
            ],
        )

    def create_chunks(
        self,
        documents: list[Document],
    ) -> list[Document]:
        """
        Split documents into smaller chunks.
        """

        chunks = self.text_splitter.split_documents(documents)

        total_chunks = len(chunks)

        # Enrich metadata for every chunk
        for index, chunk in enumerate(chunks):

            chunk.metadata["chunk_index"] = index
            chunk.metadata["total_chunks"] = total_chunks

        return chunks