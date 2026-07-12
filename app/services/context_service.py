import re

from langchain_core.documents import Document


class ContextService:
    """
    Responsible for preparing retrieved documents before
    they are sent to the LLM.
    """

    @staticmethod
    def _clean_text(text: str) -> str:

        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"\n{2,}", "\n", text)

        return text.strip()

    def build_context(
        self,
        documents: list[Document],
    ) -> tuple[str, list]:

        print("\n")
        print("=" * 100)
        print("CONTEXT SERVICE")
        print("=" * 100)

        print(f"Documents received : {len(documents)}")

        if not documents:
            print("No documents received.")
            return "", []

        documents.sort(
            key=lambda doc: doc.metadata.get(
                "start",
                0,
            )
        )

        context_parts = []
        sources = []

        previous_text = ""

        for index, document in enumerate(documents, start=1):

            print("-" * 100)
            print(f"Processing Document {index}")

            text = self._clean_text(
                document.page_content
            )

            print("\nCleaned Text:")
            print(repr(text[:300]))

            if not text:

                print("Skipped because text is empty.")
                continue

            if text == previous_text:

                print("Skipped duplicate.")
                continue

            previous_text = text

            start = round(
                document.metadata.get(
                    "start",
                    0,
                ),
                2,
            )

            end = round(
                document.metadata.get(
                    "end",
                    0,
                ),
                2,
            )

            chunk_id = document.metadata.get(
                "chunk_id",
                index,
            )

            context_parts.append(
                f"""
==================================================

EXCERPT {index}

Chunk ID : {chunk_id}

Timestamp : {start}s - {end}s

Transcript:

{text}
"""
            )

            sources.append(
                {
                    "chunk_id": chunk_id,
                    "start": start,
                    "end": end,
                }
            )

        context = "\n".join(context_parts)

        print("\n")
        print("=" * 100)
        print("FINAL CONTEXT")
        print("=" * 100)

        print(context)

        print("=" * 100)
        print(f"Context Length : {len(context)}")
        print(f"Sources : {len(sources)}")
        print("=" * 100)
        print("\n")

        return context, sources