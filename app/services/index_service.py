from app.services.block_service import BlockService
from app.services.chunk_service import ChunkService
from app.services.document_service import DocumentService
from app.services.transcript_service import TranscriptService
from app.services.transcript_storage_service import (
    TranscriptStorageService,
)
from app.services.vector_service import VectorService


class IndexService:
    """
    Handles the complete indexing pipeline.
    """

    def __init__(self):

        self.chunk_service = ChunkService()

        self.vector_service = VectorService()

        self.storage_service = TranscriptStorageService()

    def process_video(
        self,
        url: str,
    ):

        # -----------------------------
        # Video ID
        # -----------------------------

        video_id = TranscriptService.extract_video_id(
            url
        )

        # -----------------------------
        # Transcript
        # -----------------------------

        transcript = TranscriptService.fetch_transcript(
            video_id
        )

        cleaned_transcript = (
            TranscriptService.clean_transcript(
                transcript
            )
        )

        # -----------------------------
        # Save Full Transcript
        # -----------------------------

        self.storage_service.save(
            video_id=video_id,
            transcript=cleaned_transcript,
        )

        # -----------------------------
        # Blocks
        # -----------------------------

        blocks = BlockService.create_blocks(
            transcript
        )

        # -----------------------------
        # Documents
        # -----------------------------

        documents = (
            DocumentService.create_documents(
                video_id=video_id,
                blocks=blocks,
            )
        )

        # -----------------------------
        # Chunks
        # -----------------------------

        chunks = self.chunk_service.create_chunks(
            documents
        )

        # -----------------------------
        # Store Vectors
        # -----------------------------

        self.vector_service.delete_video(
            video_id
        )

        self.vector_service.add_documents(
            chunks
        )

        return {
            "status": "success",
            "video_id": video_id,
            "segments": len(transcript),
            "blocks": len(blocks),
            "documents": len(documents),
            "chunks": len(chunks),
            "message": "Video indexed successfully.",
        }