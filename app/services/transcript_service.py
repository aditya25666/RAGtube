from urllib.parse import parse_qs, urlparse

from youtube_transcript_api import (
    NoTranscriptFound,
    TranscriptsDisabled,
    YouTubeTranscriptApi,
)


class TranscriptService:
    """
    Handles YouTube transcript extraction.
    """

    @staticmethod
    def extract_video_id(url: str) -> str:
        """
        Extract the YouTube video ID from different URL formats.
        """

        parsed = urlparse(url)

        if parsed.hostname == "youtu.be":
            return parsed.path[1:]

        if parsed.hostname in (
            "youtube.com",
            "www.youtube.com",
            "m.youtube.com",
        ):
            if parsed.path == "/watch":
                query = parse_qs(parsed.query)

                if "v" not in query:
                    raise ValueError("Invalid YouTube URL")

                return query["v"][0]

            if parsed.path.startswith("/embed/"):
                return parsed.path.split("/")[2]

        raise ValueError("Invalid YouTube URL")

    @staticmethod
    def fetch_transcript(video_id: str) -> list:
        """
        Fetch the best available transcript.

        Priority:
        1. Manual English
        2. Auto-generated English
        3. Manual transcript in any language
        4. Auto-generated transcript in any language
        """

        api = YouTubeTranscriptApi()

        try:
            transcript_list = api.list(video_id)

            # 1. Manual English
            try:
                transcript = transcript_list.find_transcript(["en"])
                return transcript.fetch().to_raw_data()
            except NoTranscriptFound:
                pass

            # 2. Auto English
            try:
                transcript = transcript_list.find_generated_transcript(["en"])
                return transcript.fetch().to_raw_data()
            except NoTranscriptFound:
                pass

            # 3 & 4. First available transcript
            for transcript in transcript_list:
                return transcript.fetch().to_raw_data()

            raise NoTranscriptFound(
                video_id=video_id,
                requested_language_codes=["en"],
                transcript_data=transcript_list,
            )

        except TranscriptsDisabled:
            raise Exception("Transcripts are disabled for this video.")

        except Exception as e:
            raise Exception(f"Failed to fetch transcript: {str(e)}")

    @staticmethod
    def clean_transcript(transcript: list) -> str:
        """
        Convert transcript into a continuous string.
        """

        return " ".join(
            segment["text"].strip()
            for segment in transcript
            if segment["text"].strip()
        )