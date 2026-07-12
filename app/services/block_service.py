from typing import Any


class BlockService:
    """
    Creates larger transcript blocks from YouTube transcript segments.

    These blocks preserve timestamps and provide richer context
    for embedding generation.
    """

    @staticmethod
    def create_blocks(
        transcript: list[dict[str, Any]],
        max_chars: int = 1000,
        max_duration: int = 60,
    ) -> list[dict[str, Any]]:
        """
        Merge transcript segments into larger logical blocks.

        Args:
            transcript: Raw transcript from youtube-transcript-api
            max_chars: Maximum characters allowed in one block
            max_duration: Maximum duration (seconds) of one block

        Returns:
            List of transcript blocks.
        """

        if not transcript:
            return []

        blocks = []

        current_text = []
        current_start = None
        current_end = None

        for segment in transcript:

            text = segment.get("text", "").strip()

            if not text:
                continue

            start = segment["start"]
            end = start + segment["duration"]

            if current_start is None:
                current_start = start

            current_text.append(text)
            current_end = end

            combined_text = " ".join(current_text)

            reached_char_limit = len(combined_text) >= max_chars
            reached_time_limit = (current_end - current_start) >= max_duration

            if reached_char_limit or reached_time_limit:

                blocks.append(
                    {
                        "text": combined_text,
                        "start": current_start,
                        "end": current_end,
                    }
                )

                current_text = []
                current_start = None
                current_end = None

        if current_text:
            blocks.append(
                {
                    "text": " ".join(current_text),
                    "start": current_start,
                    "end": current_end,
                }
            )

        return blocks