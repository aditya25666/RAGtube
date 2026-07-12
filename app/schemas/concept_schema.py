from google.genai import types


CONCEPT_SCHEMA = types.Schema(
    type=types.Type.OBJECT,
    required=["concepts"],
    properties={
        "concepts": types.Schema(
            type=types.Type.ARRAY,
            description="List of important concepts explained in the video.",
            items=types.Schema(
                type=types.Type.OBJECT,
                required=[
                    "name",
                    "definition",
                    "importance",
                    "real_world_example",
                    "difficulty",
                ],
                properties={
                    "name": types.Schema(
                        type=types.Type.STRING,
                        description="Concept name.",
                    ),
                    "definition": types.Schema(
                        type=types.Type.STRING,
                        description="Simple explanation of the concept.",
                    ),
                    "importance": types.Schema(
                        type=types.Type.STRING,
                        description="Why this concept matters.",
                    ),
                    "real_world_example": types.Schema(
                        type=types.Type.STRING,
                        description="Simple real-world example.",
                    ),
                    "difficulty": types.Schema(
                        type=types.Type.STRING,
                        enum=["Easy", "Medium", "Hard"],
                        description="Difficulty level.",
                    ),
                },
            ),
        ),
    },
)