from google.genai import types


CHAT_SCHEMA = types.Schema(
    type=types.Type.OBJECT,
    required=[
        "answer",
        "confidence",
        "sources",
    ],
    properties={
        "answer": types.Schema(
            type=types.Type.STRING,
            description="Answer to the user's question."
        ),

        "confidence": types.Schema(
            type=types.Type.STRING,
            enum=[
                "High",
                "Medium",
                "Low",
            ],
            description="Confidence level."
        ),

        "sources": types.Schema(
            type=types.Type.ARRAY,
            description="Chunks used to answer.",
            items=types.Schema(
                type=types.Type.OBJECT,
                required=[
                    "chunk_index",
                ],
                properties={
                    "chunk_index": types.Schema(
                        type=types.Type.INTEGER,
                    )
                }
            )
        )
    }
)