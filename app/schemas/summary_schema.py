from google.genai import types


SUMMARY_SCHEMA = types.Schema(
    type=types.Type.OBJECT,
    required=[
        "overview",
        "learning_points",
        "detailed_summary",
        "key_takeaways",
        "conclusion",
    ],
    properties={
        "overview": types.Schema(
            type=types.Type.STRING,
            description="Overall overview of the video.",
        ),
        "learning_points": types.Schema(
            type=types.Type.ARRAY,
            description="Important learning points.",
            items=types.Schema(
                type=types.Type.STRING,
            ),
        ),
        "detailed_summary": types.Schema(
            type=types.Type.STRING,
            description="Detailed explanation following the flow of the video.",
        ),
        "key_takeaways": types.Schema(
            type=types.Type.ARRAY,
            description="Most important takeaways.",
            items=types.Schema(
                type=types.Type.STRING,
            ),
        ),
        "conclusion": types.Schema(
            type=types.Type.STRING,
            description="Overall conclusion of the video.",
        ),
    }
)