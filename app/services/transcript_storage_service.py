from pathlib import Path


class TranscriptStorageService:
    """
    Handles saving and loading transcripts from disk.
    """

    TRANSCRIPT_DIR = Path("data/transcripts")

    def __init__(self):
        self.TRANSCRIPT_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save(
        self,
        video_id: str,
        transcript: str,
    ) -> None:
        """
        Save transcript as a text file.
        """

        file_path = self.TRANSCRIPT_DIR / f"{video_id}.txt"

        file_path.write_text(
            transcript,
            encoding="utf-8",
        )

    def load(
        self,
        video_id: str,
    ) -> str:
        """
        Load transcript from disk.
        """

        file_path = self.TRANSCRIPT_DIR / f"{video_id}.txt"

        if not file_path.exists():
            raise FileNotFoundError(
                f"Transcript not found for video '{video_id}'."
            )

        return file_path.read_text(
            encoding="utf-8",
        )

    def exists(
        self,
        video_id: str,
    ) -> bool:

        file_path = self.TRANSCRIPT_DIR / f"{video_id}.txt"

        return file_path.exists()

    def delete(
        self,
        video_id: str,
    ) -> None:

        file_path = self.TRANSCRIPT_DIR / f"{video_id}.txt"

        if file_path.exists():
            file_path.unlink()